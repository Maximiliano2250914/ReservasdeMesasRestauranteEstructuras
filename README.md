
# Sistema de Reservas de Mesas en un Restaurante

## Integrantes:

Manuel Alejandro Rojas Sierra - 2250938

Jose Julian Gamboa Moreno - 2250947

David Santiago Uscategui Zubieta - 2250932

Juan David Castro Pacheco - 2250914

Maximiliano Osorio 2250914

## Resumen del proyecto

### Nuestro problema

Los restaurantes a medida que van desarrollando su modelo de negocio, se topan con la necesidad de organizar adecuadamente el espacio que ocupan sus clientes: las mesas. El metodo mas utilizado a nivel mundial para esta necesidad son las reservas, en la mayoría de casos mediante páginas web y aplicaciones. Se pueden tener ver asi: la cantidad de personas que requieren de una mesa, la fecha y la hora. Gracias a esto es posible mejorar la eficiencia con la que se disponen los recursos materiales y humanos en un restaurante, ademas de permitir que no se presenten conflictos de horario, ocupacion o filas innecesarias.

### Nuestra solucion

Crear un sistema de reservas de mesas en un restaurante, implementando funciones que nos permitan gestionar las reservas, asignar mesas y mantener un registro ordenado de las reservas realizadas.

Esto lo hacemos con metodos distintos (listas enlazadas, arboles, grafos), y despues compararemos cual de estos es mas eficiente, facil de implementar y viable para esta problematica.

## Etapas del proyecto

### Primera Entrega: Listas enlazadas

Para nuestra primera entrega se usan listas enlazadas para solucionar esta problematica. Como se puede apreciar en el codigo "primeraEntregaListas.py", el programa en Python con listas contiene las siguientes funciones:

- Verificar si la lista esta vacia
- Contar la cantidad de elementos en la lista
- Imprimir los elementos de la lista
- Agregar un elemento al inicio de la lista
- Buscar un elemento que se puede escoger en la lista

A pesar de no ser la alternativa mas viable, como veremos mas adelante, nos sirve como una base logica para entender la problematica y la solucion que debemos llevar acabo.

### Segunda Entrega: Arboles

Teniendo en cuenta la primera entrega, donde se registraba a cada persona de una reserva como un nodo independiente de una lista enlazada, podemos llevar un registro mas no es viable consultar que mesas estan disponibles en un turno especifico, pues toca recorrer toda la lista elemento a elemento y comparar uno por uno.

Por ello, en esta segunda entrega se usa un arbol jerarquico con raiz en el restaurante, segundo nivel las fechas, tercer nivel los horarios de cada dia y las hojas, que hacen parte del cuarto nivel, son las mesas reservadas con el nombre del cliente. Mediante esta estructura, si es necesario consultar disponibilidad para cierta fecha y hora, solo toca recorrer la rama que corresponda, sin mirar fechas afuera de la requerida.

En comparacion a las listas enlazadas, se halla que aparte de no tener que atravesar toda una secuencia lineal, esta estructura es mas cercana a la logica que se sigue para que un cliente realice una reserva: se define primero el restaurante, seguido de la fecha, la hora y por ultimo, la mesa.

Y con esta funcionalidad nueva con arboles, se hace entrega del codigo "segundaEntregaArboles.py". 

### Entrega Final: Grafos

Siguiendo la base logica de las entregas anteriores, ahora hacemos uso de grafos en Python, con las siguientes funciones:

- Insertar elementos
- Eliminar elementos
- Buscar elementos segun su funcionamiento

Con la implementacion de un grafo, tenemos mas flexibilidad y escalabilidad que con listas y arboles, al igual que las busquedas son eficientes mediante el recorrido de vecinos. Gracias a esto podemos crear un sistema de reserva de mesas en un restaurante util, rapido y bonito. Y asi por ultimo entregamos   "ultimaEntregaGrafos.py"

Gracias a las anteriores entregas entendemos mas la problematica y podemos apreciar los pros y contras de cada uno de estos metodos. Con cada entrega nuestro entendimiento del problema mejoro y nos ayudo a comprender la implementacion de cada metodo.