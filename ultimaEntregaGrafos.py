import time
from collections import defaultdict, deque

class Grafo:
    def __init__(self):

        self.grafo = defaultdict(dict)
        self.metadatos = {}
    
    def agregar_nodo(self, nodo, metadata=None):
        
        if nodo not in self.grafo:
            self.grafo[nodo] = {}
            self.metadatos[nodo] = metadata if metadata else {}
            return True
        return False
    
    def agregar_arista(self, origen, destino, peso=1):
       
        if origen not in self.grafo:
            self.agregar_nodo(origen)
        if destino not in self.grafo:
            self.agregar_nodo(destino)
        self.grafo[origen][destino] = peso
        return True
    
    def eliminar_nodo(self, nodo):
        
        if nodo not in self.grafo:
            return False
        
        for origen in self.grafo:
            if nodo in self.grafo[origen]:
                del self.grafo[origen][nodo]
        
        del self.grafo[nodo]
        if nodo in self.metadatos:
            del self.metadatos[nodo]
        return True
    
    def eliminar_arista(self, origen, destino):
        
        if origen in self.grafo and destino in self.grafo[origen]:
            del self.grafo[origen][destino]
            return True
        return False
    
    def buscar_nodo(self, nodo):
        
        return nodo in self.grafo
    
    def buscar_arista(self, origen, destino):
        
        return origen in self.grafo and destino in self.grafo[origen]
    
    def obtener_vecinos(self, nodo):
        
        if nodo in self.grafo:
            return list(self.grafo[nodo].keys())
        return []
    
    def obtener_peso(self, origen, destino):
        
        if self.buscar_arista(origen, destino):
            return self.grafo[origen][destino]
        return None
    
    def contar_nodos(self):
        
        return len(self.grafo)
    
    def contar_aristas(self):
        
        total = 0
        for nodo in self.grafo:
            total += len(self.grafo[nodo])
        return total
    
    def esta_vacio(self):
        
        return len(self.grafo) == 0
    
    def imprimir_grafo(self):
        
        if self.esta_vacio():
            print("\nEl grafo esta vacio")
            return
        
        print("\n ESTRUCTURA DEL GRAFO ")
        for nodo in sorted(self.grafo.keys()):
            if self.grafo[nodo]:
                conexiones = [f"{destino}(peso:{peso})" for destino, peso in self.grafo[nodo].items()]
                print(f"{nodo} --> {', '.join(conexiones)}")
            else:
                print(f"{nodo} --> (sin conexiones)")
        print()
    
    def obtener_metadatos(self, nodo):
        
        return self.metadatos.get(nodo, {})
    
    def actualizar_metadatos(self, nodo, nuevos_metadatos):
        
        if nodo in self.metadatos:
            self.metadatos[nodo].update(nuevos_metadatos)
            return True
        return False



class SistemaReservasGrafo:
    def __init__(self):
        self.grafo = Grafo()
        self.grafo.agregar_nodo("RESTAURANTE", {"tipo": "raiz"})
        self.mesas_totales = ["Mesa_1", "Mesa_2", "Mesa_3", "Mesa_4", "Mesa_5"]
    
    def crear_fecha(self, fecha):
        
        nodo_fecha = f"FECHA_{fecha}"
        if not self.grafo.buscar_nodo(nodo_fecha):
            self.grafo.agregar_nodo(nodo_fecha, {"tipo": "fecha", "valor": fecha})
            self.grafo.agregar_arista("RESTAURANTE", nodo_fecha, peso=1)
        return nodo_fecha
    
    def crear_hora(self, fecha, hora):
        
        nodo_fecha = self.crear_fecha(fecha)
        nodo_hora = f"FECHA_{fecha}_HORA_{hora}"
        if not self.grafo.buscar_nodo(nodo_hora):
            self.grafo.agregar_nodo(nodo_hora, {"tipo": "hora", "valor": hora, "fecha": fecha})
            self.grafo.agregar_arista(nodo_fecha, nodo_hora, peso=1)
        return nodo_hora
    
    def agregar_reserva(self, fecha, hora, mesa, nombre_cliente, num_personas=2):
        
        nodo_hora = self.crear_hora(fecha, hora)
        nodo_mesa = f"FECHA_{fecha}_HORA_{hora}_{mesa}"

        if self.grafo.buscar_nodo(nodo_mesa):
            print(f"\n La {mesa} ya está ocupada el {fecha} a las {hora}")
            return False

        self.grafo.agregar_nodo(nodo_mesa, {
            "tipo": "reserva",
            "mesa": mesa,
            "cliente": nombre_cliente,
            "personas": num_personas,
            "fecha": fecha,
            "hora": hora
        })

        self.grafo.agregar_arista(nodo_hora, nodo_mesa, peso=num_personas)
        
        print(f"\n Reserva registrada exitosamente:")
        print(f"   Cliente: {nombre_cliente}")
        print(f"   Mesa: {mesa}")
        print(f"   Fecha: {fecha}")
        print(f"   Hora: {hora}")
        print(f"   Personas: {num_personas}")
        return True
    
    def eliminar_reserva(self, fecha, hora, mesa):
        
        nodo_mesa = f"FECHA_{fecha}_HORA_{hora}_{mesa}"
        
        if not self.grafo.buscar_nodo(nodo_mesa):
            print(f"\n No existe reserva para {mesa} el {fecha} a las {hora}")
            return False
        
        metadatos = self.grafo.obtener_metadatos(nodo_mesa)
        self.grafo.eliminar_nodo(nodo_mesa)
        print(f"\n Reserva eliminada: {mesa} - Cliente: {metadatos.get('cliente', 'N/A')}")
        return True
    
    def buscar_reserva_cliente(self, nombre_cliente):
        
        reservas_encontradas = []
        
        for nodo in self.grafo.grafo.keys():
            metadatos = self.grafo.obtener_metadatos(nodo)
            if metadatos.get("tipo") == "reserva" and metadatos.get("cliente") == nombre_cliente:
                reservas_encontradas.append({
                    "nodo": nodo,
                    "mesa": metadatos.get("mesa"),
                    "fecha": metadatos.get("fecha"),
                    "hora": metadatos.get("hora"),
                    "personas": metadatos.get("personas")
                })
        
        if reservas_encontradas:
            print(f"\n Reservas encontradas para {nombre_cliente}:")
            for i, res in enumerate(reservas_encontradas, 1):
                print(f"   {i}. {res['mesa']} - {res['fecha']} a las {res['hora']} ({res['personas']} personas)")
        else:
            print(f"\n No se encontraron reservas para {nombre_cliente}")
        
        return reservas_encontradas
    
    def consultar_disponibilidad(self, fecha, hora):
        
        nodo_hora = f"FECHA_{fecha}_HORA_{hora}"
        
        if not self.grafo.buscar_nodo(nodo_hora):
            print(f"\n Todas las mesas estan disponibles el {fecha} a las {hora}")
            print(f"   Mesas: {', '.join(self.mesas_totales)}")
            return self.mesas_totales
        
        
        vecinos = self.grafo.obtener_vecinos(nodo_hora)
        mesas_ocupadas = []
        
        for vecino in vecinos:
            metadatos = self.grafo.obtener_metadatos(vecino)
            if metadatos.get("tipo") == "reserva":
                mesas_ocupadas.append(metadatos.get("mesa"))
        
        
        mesas_disponibles = [m for m in self.mesas_totales if m not in mesas_ocupadas]
        
        if mesas_disponibles:
            print(f"\n Mesas disponibles el {fecha} a las {hora}:")
            for mesa in mesas_disponibles:
                print(f"   - {mesa}")
        else:
            print(f"\n No hay mesas disponibles el {fecha} a las {hora}")
        
        return mesas_disponibles
    
    def listar_todas_reservas(self):
        
        reservas = []
        
        for nodo in self.grafo.grafo.keys():
            metadatos = self.grafo.obtener_metadatos(nodo)
            if metadatos.get("tipo") == "reserva":
                reservas.append(metadatos)
        
        if not reservas:
            print("\n No hay reservas en el sistema")
            return []
        
        print("\n TODAS LAS RESERVAS:")
        reservas_ordenadas = sorted(reservas, key=lambda x: (x.get("fecha", ""), x.get("hora", "")))
        
        for i, res in enumerate(reservas_ordenadas, 1):
            print(f"{i}. {res.get('fecha')} {res.get('hora')} - {res.get('mesa')} - "
                  f"{res.get('cliente')} ({res.get('personas')} personas)")
        
        return reservas_ordenadas
    
    def mostrar_ocupacion_fecha(self, fecha):
        
        nodo_fecha = f"FECHA_{fecha}"
        
        if not self.grafo.buscar_nodo(nodo_fecha):
            print(f"\n No hay reservas para {fecha}")
            return
          
        horas = self.grafo.obtener_vecinos(nodo_fecha)
        
        print(f"\n OCUPACIÓN DEL {fecha}:")
        for nodo_hora in sorted(horas):
            metadatos_hora = self.grafo.obtener_metadatos(nodo_hora)
            hora = metadatos_hora.get("valor", "")

            reservas_hora = self.grafo.obtener_vecinos(nodo_hora)
            num_reservas = len(reservas_hora)
            
            print(f"\n   {hora}: {num_reservas}/{len(self.mesas_totales)} mesas ocupadas")
            
            if num_reservas > 0:
                for reserva_nodo in reservas_hora:
                    meta_res = self.grafo.obtener_metadatos(reserva_nodo)
                    print(f"     - {meta_res.get('mesa')}: {meta_res.get('cliente')} "
                          f"({meta_res.get('personas')} personas)")


def menu_principal():
    sistema = SistemaReservasGrafo()
    
    while True:
        menu = """

   SISTEMA DE RESERVAS - GRAFO              


1.   Ver estado del grafo (vacio/lleno)
2.   Contar nodos y aristas
3.   Imprimir estructura del grafo
4.   Agregar reserva
5.   Eliminar reserva
6.   Buscar reservas por cliente
7.   Consultar disponibilidad
8.   Listar todas las reservas
9.   Ver ocupacion por fecha
10.  Operaciones avanzadas del grafo
11.  Salir

Ingrese una opción: """
        
        try:
            opc = int(input(menu))
        except ValueError:
            print("\n Opcion invalida, intente nuevamente.")
            time.sleep(1.5)
            continue
        
        if opc == 1:
            if sistema.grafo.esta_vacio():
                print("\n El grafo esta vacio")
            else:
                print(f"\n El grafo contiene {sistema.grafo.contar_nodos()} nodos")
            time.sleep(1.5)
        
        elif opc == 2:
            nodos = sistema.grafo.contar_nodos()
            aristas = sistema.grafo.contar_aristas()
            print(f"\n Estadisticas del grafo:")
            print(f"   Nodos: {nodos}")
            print(f"   Aristas: {aristas}")
            time.sleep(2)
        
        elif opc == 3:
            sistema.grafo.imprimir_grafo()
            input("\nPresione ENTER para continuar...")
        
        elif opc == 4:
            print("\n NUEVA RESERVA")
            fecha = input("Fecha (ano/mes/dia): ")
            hora = input("Hora (horas:minutos): ")
            print(f"\nMesas disponibles: {', '.join(sistema.mesas_totales)}")
            mesa = input("Mesa (ej. Mesa_1): ")
            nombre = input("Nombre del cliente: ")
            try:
                personas = int(input("Numero de personas: "))
                sistema.agregar_reserva(fecha, hora, mesa, nombre, personas)
            except ValueError:
                print(" Numero de personas invalido")
            time.sleep(2)
        
        elif opc == 5:
            print("\n ELIMINAR RESERVA")
            fecha = input("Fecha (ano/mes/dia): ")
            hora = input("Hora (horas:minutos): ")
            mesa = input("Mesa (ej. Mesa_1): ")
            sistema.eliminar_reserva(fecha, hora, mesa)
            time.sleep(2)
        
        elif opc == 6:
            print("\n BUSCAR RESERVAS")
            nombre = input("Nombre del cliente: ")
            sistema.buscar_reserva_cliente(nombre)
            time.sleep(2)
        
        elif opc == 7:
            print("\n CONSULTAR DISPONIBILIDAD")
            fecha = input("Fecha (ano/mes/dia): ")
            hora = input("Hora (horas:minutos): ")
            sistema.consultar_disponibilidad(fecha, hora)
            time.sleep(2)
        
        elif opc == 8:
            sistema.listar_todas_reservas()
            input("\nPresione ENTER para continuar...")
        
        elif opc == 9:
            print("\n OCUPACION POR FECHA")
            fecha = input("Fecha (ano/mes/dia): ")
            sistema.mostrar_ocupacion_fecha(fecha)
            input("\nPresione ENTER para continuar...")
        
        elif opc == 10:
            menu_avanzado(sistema)
        
        elif opc == 11:
            print("\n Saliendo del sistema...")
            time.sleep(1)
            break
        
        else:
            print("\n Opción invalida")
            time.sleep(1.5)


def menu_avanzado(sistema):
    
    while True:
        menu = """

   OPERACIONES AVANZADAS DEL GRAFO          


1. Agregar nodo personalizado
2. Agregar arista personalizada
3. Eliminar nodo especifico
4. Eliminar arista específica
5. Buscar nodo
6. Buscar arista
7. Ver vecinos de un nodo
8. Ver peso de una arista
9. Ver metadatos de un nodo
10. Volver al menu principal

Ingrese una opción: """
        
        try:
            opc = int(input(menu))
        except ValueError:
            print("\n Opcion invalida")
            time.sleep(1)
            continue
        
        if opc == 1:
            nodo = input("\nNombre del nodo: ")
            tipo = input("Tipo (ej. personalizado): ")
            if sistema.grafo.agregar_nodo(nodo, {"tipo": tipo}):
                print(f" Nodo '{nodo}' agregado")
            else:
                print(f" El nodo '{nodo}' ya existe")
            time.sleep(1.5)
        
        elif opc == 2:
            origen = input("\nNodo origen: ")
            destino = input("Nodo destino: ")
            try:
                peso = float(input("Peso de la arista: "))
                sistema.grafo.agregar_arista(origen, destino, peso)
                print(f" Arista {origen} -> {destino} (peso: {peso}) agregada")
            except ValueError:
                print(" Peso invalido")
            time.sleep(1.5)
        
        elif opc == 3:
            nodo = input("\nNodo a eliminar: ")
            if sistema.grafo.eliminar_nodo(nodo):
                print(f" Nodo '{nodo}' eliminado")
            else:
                print(f" El nodo '{nodo}' no existe")
            time.sleep(1.5)
        
        elif opc == 4:
            origen = input("\nNodo origen: ")
            destino = input("Nodo destino: ")
            if sistema.grafo.eliminar_arista(origen, destino):
                print(f" Arista {origen} -> {destino} eliminada")
            else:
                print(f" La arista no existe")
            time.sleep(1.5)
        
        elif opc == 5:
            nodo = input("\nNodo a buscar: ")
            if sistema.grafo.buscar_nodo(nodo):
                print(f" El nodo '{nodo}' existe")
            else:
                print(f" El nodo '{nodo}' no existe")
            time.sleep(1.5)
        
        elif opc == 6:
            origen = input("\nNodo origen: ")
            destino = input("Nodo destino: ")
            if sistema.grafo.buscar_arista(origen, destino):
                peso = sistema.grafo.obtener_peso(origen, destino)
                print(f" La arista {origen} -> {destino} existe (peso: {peso})")
            else:
                print(f" La arista no existe")
            time.sleep(1.5)
        
        elif opc == 7:
            nodo = input("\nNodo: ")
            vecinos = sistema.grafo.obtener_vecinos(nodo)
            if vecinos:
                print(f"\n Vecinos de '{nodo}':")
                for v in vecinos:
                    peso = sistema.grafo.obtener_peso(nodo, v)
                    print(f"   -> {v} (peso: {peso})")
            else:
                print(f" El nodo no existe o no tiene vecinos")
            time.sleep(2)
        
        elif opc == 8:
            origen = input("\nNodo origen: ")
            destino = input("Nodo destino: ")
            peso = sistema.grafo.obtener_peso(origen, destino)
            if peso is not None:
                print(f"  Peso de {origen} -> {destino}: {peso}")
            else:
                print(" La arista no existe")
            time.sleep(1.5)
        
        elif opc == 9:
            nodo = input("\nNodo: ")
            metadatos = sistema.grafo.obtener_metadatos(nodo)
            if metadatos:
                print(f"\n Metadatos de '{nodo}':")
                for clave, valor in metadatos.items():
                    print(f"   {clave}: {valor}")
            else:
                print(" El nodo no existe o no tiene metadatos")
            time.sleep(2)
        
        elif opc == 10:
            break
        
        else:
            print("\n Opcion inválida")
            time.sleep(1)


if __name__ == "__main__":
    menu_principal()
