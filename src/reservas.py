
import random
def bienvenida():
 
    señor=input("usted es señor o señora?:")

    nombre=input("introduzca su nombre:")

    apellido=input("introduzca su apellido:")

    print(f"bienvenido {señor} {nombre} {apellido} a flylift ")
 
def selecciona_vuelo():
 
    print("seleccione su ciudad de origen:")

    print("1.Medellin\n2.Cartagena\n3.Bogota.")

    ciudad1=int(input("ingrese el numero de la ciudad de origen:"))


    ciudad2= int(input("ingrese el numero de la ciudad destino:"))
 
 
 
    
    dia_semana=input("digite el  dia de la semana que desea viajar(por ejemplo lunes):").upper()

    dia_numero=int(input("digite el dia de la semana que va a viajr(1-30):"))

    return ciudad1,ciudad2,dia_semana,dia_numero
 
 
 
 
def calcular_precio(ciudad1, ciudad2, dia_semana):
    if ciudad1 == 1 and ciudad2 == 2 and (dia_semana == "LUNES" or dia_semana == "MARTES" or dia_semana == "MIÉRCOLES" or dia_semana == "JUEVES"):
        boleto = "Su boleto tiene un costo de 79.900 pesos"


    elif ciudad1 == 1 and ciudad2 == 2 and (dia_semana == "VIERNES" or dia_semana == "SÁBADO" or dia_semana == "DOMINGO"):
        boleto = "Su boleto tiene un costo de 119.000 pesos"

    elif ciudad1 == 1 and ciudad2 == 3 and (dia_semana == "LUNES" or dia_semana == "MARTES" or dia_semana == "MIÉRCOLES" or dia_semana == "JUEVES"):
        boleto = "Su boleto tiene un costo de 156.900 pesos"


    elif ciudad1 == 1 and ciudad2 == 3 and (dia_semana == "VIERNES" or dia_semana == "SÁBADO" or dia_semana == "DOMINGO"):
        boleto = "Su boleto tiene un costo de 213.000 pesos"


    elif ciudad1 == 2 and ciudad2 == 3 and (dia_semana == "LUNES" or dia_semana == "MARTES" or dia_semana == "MIÉRCOLES" or dia_semana == "JUEVES"):
        boleto = "Su boleto tiene un costo de 156.900 pesos"

        
    elif ciudad1 == 2 and ciudad2 == 3 and (dia_semana == "VIERNES" or dia_semana == "SÁBADO" or dia_semana == "DOMINGO"):
        boleto = "Su boleto tiene un costo de 213.000 pesos"
    else:
        boleto = "No hay vuelos disponibles para esta ruta."

    return boleto




def asignacion_asiento():
    preferencia=int(input("En que lugar de la aeronave desea localizarse si prefiere un asiento cerca ala ventana digete 1, si prefiere en el pasillo digite 2 o si no teine preferencia digite 3:"))


    
    numeros=random.randint(1,29)

    if preferencia == 1:
         letra ="A"

    elif preferencia == 2:
         letra ="B"
    else:
         letra ="c"
    
    return numeros,letra


def main():
    bienvenida()

    ciudad1, ciudad2, dia_semana, dia_numero = selecciona_vuelo()

    

    asiento_numero, asiento_letra = asignacion_asiento()

    precio = calcular_precio(ciudad1, ciudad2, dia_semana)

    print(precio)


    print(f"Su asiento es: {asiento_numero}{asiento_letra}")

    







if __name__ == "__main__":
    main()
