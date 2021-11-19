# Ejercicios en python3

    1. Resuelva el siguiente problema creando una aplicación en el lenguaje que desee:
En un centro de entrega de una compañía de envío de paquetes, una computadora decide cuales paquetes serán cargados en los camiones de la compañía. 

Todos los espacios en los camiones son clasificados como unidades de tamaño, los cuales son representados con números enteros. Cada tipo de camión, tiene sus propias unidades de tamaño. Así mismo, cada paquete ocupará una cantidad de unidades de tamaño específica.

Teniendo en cuenta un listado de paquetes y el tamaño del camión (parámetros de entrada), se debe crear un programa que se encargue de determinar, exactamente, una pareja de paquetes que se puedan cargar en el camión. 

<b>Reglas de negocio</b>:
        <li>a. El camión debe reservar 30 unidades de tamaño siempre, por seguridad. 
        <li>b. Se cargarán exactamente dos paquetes por camión, cuyo tamaño sumado permita dejar exactamente 30 unidades de tamaño libres en el camión.
        <li>c. No se puede escoger el mismo paquete dos veces.
        <li>d. Si existe la posibilidad de cargar dos pares de paquetes en el camión, se debe escoger el par que tenga el paquete más grande.

<b>Parámetros de entrada:</b>
    a. TamaioCamion: Un entero que representa el tamaño del camión.
    b. Paquetes: Listado de enteros que representa el número de unidades de tamaño que ocupará cada paquete en el camión. 

Salida/Retorno:
Listado de enteros que contiene los dos paquetes seleccionados para ser cargados en el camión. 

<b>Ejemplo</b>:
Tamaño del Camión: 90
<br>
Paquetes: [10, 60, 40, 35, 20]
<br>
Resultado: [40,20] -> La suma de los paquetes es 60, lo que permite dejar las 30 unidades de espacio requeridas.

    2. Resuelva el siguiente problema creando una aplicación en el lenguaje que desee:

Una cola de clientes que va a comprar helado está esperando que la heladería abra sus puertas. Cada cliente va a comprar `solamente un` helado que vale `$5`.
La heladería tiene una política de aceptar `solamente` billetes de las siguientes denominaciones: `$5, $10 y $20`.

El saldo de la caja de la heladería al iniciar las ventas es de `$0`.

Con base en la información descrita anteriormente, se debe elaborar un programa que evalúe si es posible devolver el cambio a cada uno de los clientes en la cola cuando aplique. Al ser una cola, se debe atender a los clientes siguiendo el `esquema FIFO`.

Parámetros de Entrada:
    a. `Pagos`: Listado de enteros que representa el valor del billete con el que realizará el pago cada cliente.
`Salida`:
Indicador S o N para determinar si es posible devolver cambio a todos los clientes.

<b>Ejemplos:

    • [5,5,5,10,20] -> Retorna S
    • [5,5,10] -> Retorna S
    • [10,10] -> Retorna N

