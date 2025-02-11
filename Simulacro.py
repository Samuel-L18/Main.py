Meta_Agua = 2000  
# ml
volumen_total = 0
porciones = 0

#El agua consumida por Juan es de 2000 ml. Cada porción de agua debe ser de 100 ml a 400 ml.

while volumen_total < Meta_Agua : 
    volumen = int(input("Ingrese el volumen de agua consumido (ml): "))
    if 100 <= volumen <= 400:
        volumen_total += volumen
        porciones += 1
        print(f"Volumen total: {volumen_total} ml")
        print(f"Porciones: {porciones}")
    elif volumen < 100:

        print("Porción no válida. Ingrese un volumen entre 100 ml y 400 ml.")

print(f"¡Felicidades! {volumen_total} ml de agua en {porciones} porciones.")