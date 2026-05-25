class Nodo:
    def __init__(self, data, prioridad):
        self.data=data
        self.siguiente=None
        self.prioridad=prioridad

class ListaSE:
    def __init__(self):
        self.cabeza=None

    def vacio(self):
        if self.cabeza is None:
            print("Está vacía")
            return True
        else:
            print("Lista no vacía")
            return False
        
    def contador(self):
        contador = 0
        nodoesp = self.cabeza
        while nodoesp is not None:
            contador += 1
            nodoesp = nodoesp.siguiente
        return contador
    
    def buscador(self,data):
        nodoesp=self.cabeza
        while nodoesp!=None:
            if nodoesp.data==data:
                print("Si tiene una reserva")
                return True
            nodoesp = nodoesp.siguiente
        print("No tiene reserva")
        return False
        
    def agregar(self,data,prioridad):
        nuevoNodo=Nodo(data,prioridad)
        if self.cabeza is None:
            self.cabeza=nuevoNodo
            return
        elif nuevoNodo.prioridad<=self.cabeza.prioridad:
            nuevoNodo.siguiente=self.cabeza
            self.cabeza=nuevoNodo
            return
        actual=self.cabeza
        while actual.siguiente is not None and actual.siguiente.prioridad<=prioridad:
            actual=actual.siguiente
        nuevoNodo.siguiente = actual.siguiente
        actual.siguiente = nuevoNodo

    def imprimir(self):
        nodo_actual = self.cabeza
        while nodo_actual:
            print(nodo_actual.data)
            nodo_actual = nodo_actual.siguiente

listaO=ListaSE()

cent=0
while cent!=6:
    print("Seleccione una opcion")
    opc=int(input("1. Agregar una reserva, 2. Contar los elementos, 3. Mostrar las reservas, 4. Confirmar si esta vacia, 6. Salir"))
    if opc==1:
        nump=int(input("De cuantas personas es la reserva?: "))
        if nump<=8 and nump>0:
            fecha=str(input("Digite la fecha de la reserva (ZZZZ/YY/XX): "))
            hora=str(input("Digite la hora de su reserva (XX:XX): "))
            prio=fecha+" "+hora
            for i in range (1,nump+1):
                nom=str(input("Nombre de la persona: "))
                ced=int(input("Numero de cedula: "))
                tel=int(input("Numero de telefono: "))
                listaO.agregar({"Nombre":nom,"Cedula":ced,"Telefono":tel},prio)
        else:
            print("La reserva es muy grande, comuniquese con el restaurante")
    elif opc==2:
        print(f"Hay {listaO.contador()} personas")
    elif opc==3:
        listaO.imprimir()
    elif opc==4:
        listaO.vacio()
    elif opc==5:
        print("Seleccione una opcion")
        opc2=int(input("1. Por nombre, 2. Por cedula"))
        if opc2==1:
            bus=str(input("Digite el nombre de la persona a buscar: "))
            listaO.buscador(bus)
        elif opc2==2:
            bus=int(input("Digite la cedula a buscar: "))
            listaO.buscador(bus)
        else:
            print("Opcion invalida")
    elif opc==6:
        cent=6
    else:
        print("Opcion invalida")
