#!/usr/bin/python3
""" Aplicación Cola de Helados """

pagos = []
CAJA = []
LENGTH = 0


def helados():

    # Los parametros de entrada será un listado de enteros separados por un espacio en blanco
    # desde la consola
    myList = input(" \n \
        Entre la lista de pagos \n \
        (solo números enteros separados por \n \
        espacios en blanco): ").split(" ")

    # Si no mandan nada significa que la cola esta vacia y termina el programa.
    if myList == ['']:
        print('La cola esta vacia. Bye!')
        return

    # Se agregan los datos a la lista
    for num in myList:
        pagos.append(int(num))

    # Se comprueban los valores de los billetes o tipo de pago, si no son los esperados
    # se envia un mensaje para rectificar las entradas y termina el programa
    for b in pagos:
        if b != 5 and b != 10 and b != 20:
            print('Solo se aceptan pagos en billetes de 5, 10 y 20')
            print('N')
            return

    # Se evaluan la entrada a la caja y el tipo de pago del listado recibido.
    for p in pagos:

        # Si la caja esta vacia no puede recibir billetes > 5
        if CAJA == [] and p > 5:
            print('N')
            return

        # Agregamos lo billetes  de  5 a la caja
        elif CAJA == [] and p == 5:
            CAJA.append(p)
            LENGTH = len(CAJA)

        # Agregamos lo billetes  de  5 a la caja
        elif CAJA[0] == 5 and p == 5:
            CAJA.append(p)
            LENGTH = len(CAJA)

        # Sacamos uno de 5  y agregamos uno de 10
        elif CAJA[0] == 5 and LENGTH >= 1 and p == 10:
            CAJA.remove(5)
            CAJA.append(p)
            LENGTH = len(CAJA)

        # Si el primer billete que entró es uno de 5, no tengo cambio para uno de 20
        elif CAJA[0] == 5 and LENGTH == 1 and p == 20:
            print('N')
            return

        # Caso extremo
        elif (CAJA[0] == 10 and LENGTH >= 1) and (p == 20 or p == 10):
            if p == 20 and sum(CAJA) == 15:
                CAJA.remove(10)
                CAJA.remove(5)
                CAJA.append(p)
                continue
            else:
                print('N')
                return

        elif CAJA[0] == 10 and LENGTH == 1 and p == 5:
            CAJA.append(p)
            LENGTH = len(CAJA)
            continue

    print('S')
    return


helados()
