def datos_satelite():

    altitud_inicial = int(input("Altitud inicial del satélite (en km): "))
    arrastre = float(input("Ingrese el coeficiente de arrastre inicial: "))
    altitud_segura = int(input("Ingrese la altitud mínima segura (en km): "))
    
    
    return altitud_inicial, arrastre, altitud_segura  


def calculo(altitud_actual, altitud_segura, arrastre):
    
    contador_orbitas = 0
    

    while altitud_actual > altitud_segura:
       
        altitud_perdida = arrastre * altitud_actual
        altitud_actual -= altitud_perdida  

        
        arrastre += 0.0001
        contador_orbitas += 1  
       
        print(f"orbita {contador_orbitas}: Altitud actual = {altitud_actual} km, coeficiente de arrastre = {arrastre}")

        
        if altitud_perdida < 0.001:
            print(f"El satélite se ha estabilizado en {contador_orbitas} orbitas")
            print(f"Altitud final = {altitud_actual} km")
            break
    
    
    if altitud_actual <= altitud_segura:
        print(f"El satélite ha reingresado en la atmósfera terrestre después de {contador_orbitas} orbitas")
        print(f"Altitud final = {altitud_actual} km.")


def main():
   
    altitud_inicial, arrastre, altitud_segura = datos_satelite()
    
   
    calculo(altitud_inicial, altitud_segura, arrastre)


if __name__ == "__main__":
    main()
