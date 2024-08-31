## Analisis del probelma 1
Estamos deseñando un codigo que le permita al usuario saber cuanto debe pagar por su vuelo de acuerdona las diferentes variables que el usuario debe elegir como el trayecto el asiento y el equipaje,ademas el usuario de ingrsesar sus datos perosonales lo cual le permite conectar sus datos personles direcatamente con la aerolinea

## Variables:

- Nombre del usuario
- ciudad de origen
- ciduada destino
- Dia del viaje 
- mes del viaje
- precio del tikete 
- distancia
- asiento si/no
- pasillo del asiento
- numero de asiento

## Diagrma de flujo 

[https://miro.com/welcomeonboard/VFIyOW43NmlXZms1T0tVTERNajZpZ0NVaVBsYjlwSmZwNmxIMW1TMXEyM2o1VWd6ZDRLVDZ3Mjd5NDlBQ1QxNXwzNDU4NzY0NTk4NDMyMTI2ODIxfDI=?share_link_id=454112370949](URL)

## Pseudocodigo

INICIO

    Leer título, 
    leer nombrr
    leer apellido
    
    Mostrar saludo con nombre_completo

    Leer origen
    leer destino
    si origen == destino entonces:
        Mostrar error y finlizar
    FIN SI

    Leer semana
    leer mes

    
    SI origen y destino son Medellín, Bogota  entoces
        distancia = 240
    SI origen y destino son Medellin, Cartagena entoces
        distancia = 461
    SI origen y destino son Bogota, Cartagena entoces
        distancia = 657

    #Calcular precio
    si distancia < 400 entonces
        precio = si semana entre lunes y jueves entoces 79900 
    si no
        precio = si dia_semana entre lunes y jueves entoces 156900 
        si no 213000

    Leer preferencia 
    letrasiento = C 
    si no
     preferencia == pasillo
     si no A SI preferencia == ventana
        si no B

    numero_asiento = número aleatorio entre 1 y 29
    asiento_asignado = numero_asiento + letra_asiento

    Mostrar nombre_completo, origen, destino, dia_semana, dia_mes, precio, asiento_asignado

FIN
