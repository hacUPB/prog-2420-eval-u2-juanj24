## Analisis del problema 2
En este problema se va a simular la desintegracion de un satelito por resistencia atmosfericA

## Variables
- altitud actual
- ceficiente de arrastre
- altitud de seguridad

## Diagrma de flujo 

[https://miro.com/welcomeonboard/bWpQRUZPOFI4S1NvVkU4S1dycDEyVWdBY0FLSGJOeUpWT0RsVXF3RFF0S2d1aHFDT0FKN0xvQjRkMjdZRHVhRnwzNDU4NzY0NTk4NDMyMTI2ODIxfDI=?share_link_id=911485575277](URL)

## pseudocodigo

INICIO


    Leer altitud inicial
    Leer coeficiente_arrastre 
    Leer altitud_minima_seguridad

    
    altitud_actual = altitud inicial
    coeficiente_arrastre = coeficiente arrastre
    orbitas = 0

    #desintegracion
    minetras altitud_actual > altitud_minima 
        orbitas += 1
        altitud_perdida = coeficiente_arrastre * altitud_actual
        altitud_actual -= altitud_perdida
        coeficiente_arrastre += 0.0001

        #perdida
        SI altitud_perdida < 0.01 entoces
            Mostrar El satelite se ha estabilizado en una órbita baja
            Mostrar Altitud final , altitud_actual
            Mostrar Número de órbitas completadas
            

    
    Mostrar "El satélite ha reingresado en la atmósfera terrestre."
    Mostrar "Número total de órbitas completadas:", orbitas

FIN
