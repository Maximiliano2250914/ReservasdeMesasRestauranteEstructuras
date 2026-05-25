import time

from bigtree import print_tree
from bigtree import Node

def buscar(nodo,nom):
    if nodo.name==nom:
        return nodo
    else:
        for i in nodo.children:
            encon=buscar(i,nom)
            if encon:
                return encon

def agregar_reserva(root,fecha,hora,mesa,nombre):
    nodo_fecha=buscar(root,fecha)
    if nodo_fecha is None:
        nodo_fecha=Node(fecha,parent=root)
    nodo_hora=buscar(nodo_fecha,hora)
    if nodo_hora is None:
        nodo_hora=Node(hora,parent=nodo_fecha)
    nodo_mesa=buscar(nodo_hora,mesa)
    if nodo_mesa is None:
        Node(mesa+" | "+nombre,parent=nodo_hora)
        print(f"\nReserva registrada: {mesa} el {fecha} a las {hora} a nombre de {nombre}")
    else:
        print(f"\nEsa mesa ya está ocupada en esa fecha y hora")
    time.sleep(1.75)

def consultar_disponibilidad(root,fecha,hora):
    mesas_totales=["Mesa 1","Mesa 2","Mesa 3","Mesa 4","Mesa 5"]
    nodo_fecha=buscar(root,fecha)
    if nodo_fecha is None:
        print(f"\nTodas las mesas están disponibles el {fecha} a las {hora}")
        time.sleep(1.75)
        return
    nodo_hora=buscar(nodo_fecha,hora)
    if nodo_hora is None:
        print(f"\nTodas las mesas están disponibles el {fecha} a las {hora}")
        time.sleep(1.75)
        return
    ocupadas=[i.name.split(" | ")[0] for i in nodo_hora.children]
    libres=[m for m in mesas_totales if m not in ocupadas]
    if libres:
        print(f"\nMesas disponibles el {fecha} a las {hora}:")
        for m in libres:
            print(f"  - {m}")
    else:
        print(f"\nNo hay mesas disponibles el {fecha} a las {hora}")
    time.sleep(1.75)

root=Node("Restaurante")

while True:
    menu = """
---Menú de Opciones---

1. Vacuidad
2. Cantidad de elementos
3. Imprimir el árbol
4. Ingresar
5. Buscar
6. Consultar disponibilidad de mesas
7. Agregar reserva
8. Salir

Ingrese una opción: """

    try:
        opc = int(input(menu))
    except ValueError:
        print("\n Opción invalida, por favor intentelo nuevamente.")
        time.sleep(1.5)
        continue

    match opc:
        case 1:
            if not root.children:
                print("\nEl arbol se encuentra vacio")
                time.sleep(1.5)
            else:
                print("\nEl arbol no se encuentra vacio")
                time.sleep(1.5)

        case 2:
            cont=0
            for i in root.descendants:
                cont+=1
            print(f"\nHay {cont+1} nodos en el árbol")
            time.sleep(1.75)

        case 3:
            print_tree(root)
            time.sleep(1.5)

        case 4:
            cent2=0
            while cent2!=2:
                print("Desea continuar añadiendo nodos?")
                submenu ="""
                1. Continuar 
                2. Salir:
                Ingrese una opción: """
                opc2 = int(input(submenu))
                if opc2==1:
                    a=str(input("Digite el nombre del nodo: "))
                    nombre=str(input("Digite el padre del nodo: "))
                    padre=buscar(root,nombre)
                    if padre:
                        Node(a,parent=padre)
                    else:
                        print("Padre no encontrado")
                        time.sleep(1.5)
                elif opc2==2:
                    cent2=2
                else:
                    print("Opción invalida")
                    time.sleep(1.75)

        case 5:
            bus=str(input("\nDigite el nodo a buscar: "))
            node=buscar(root,bus)
            if node is None:
                print(f"El nodo {bus} no existe")
                time.sleep(1.5)
            else:
                print(f"El nodo {bus} sí existe")
                time.sleep(1.5)

        case 6:
            fecha=str(input("\nDigite la fecha a consultar (AAAA/MM/DD): "))
            hora=str(input("Digite la hora a consultar (HH:MM): "))
            consultar_disponibilidad(root,fecha,hora)

        case 7:
            fecha=str(input("\nDigite la fecha de la reserva (AAAA/MM/DD): "))
            hora=str(input("Digite la hora de la reserva (HH:MM): "))
            print("\nMesas disponibles: Mesa 1, Mesa 2, Mesa 3, Mesa 4, Mesa 5")
            mesa=str(input("Digite el nombre de la mesa (ej: Mesa 1): "))
            nombre=str(input("Digite el nombre del cliente: "))
            agregar_reserva(root,fecha,hora,mesa,nombre)

        case 8:
            print("\nSaliendo del programa...")
            time.sleep(1.25)
            break

        case _:
            print("Opción invalida")
            time.sleep(1.5)
