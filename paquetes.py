#!/usr/bin/python3

from itertools import combinations

RE = 0
paquetes = []

# Introducir el Tipo de Camión
TC = input('Entre el Tipo de Camion: ')

# Introducir lista de paquetes separados por espacios en blanco
myList = input("Entre la lista de paquetes: ").split(" ")
# print(myList) Esta linea es para probar en caso de falla, favor conservar

# Castear cada elemento de myList en enteros
for num in myList:
    paquetes.append(int(num))


def permut(TC, paquetes):
    """ metodo paquetes """

    # Crea una combinación única de cada dos elementos y los devuelve como una tupla
    myPermut = list(combinations(paquetes, 2))
    # print(myPermut)

    # Suma cada uno de los elementos dentro de una tupla y
    # devuelve el resultado de la suma cada tupla
    myList1 = list(map(sum, myPermut))
    # print(myList1)

    # Reserva el espacio de seguridad
    RE = int(TC) - 30

    # Halla el indice del valor calculado en RE, Si no está en la lista mandará la exepción
    try:
        myList1.index(RE)
    except ValueError:
        print(str(RE) + ' is not in list')
        return

    # Halla la tupla que contiene los paquetes acorde a los requerimientos
    print(myPermut[myList1.index(RE)])


# Llamando a la funcion permut
permut(TC, paquetes)
