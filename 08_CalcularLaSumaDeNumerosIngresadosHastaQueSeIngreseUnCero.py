suma = 0
while True:
    numero = int(input("Ingrese un número (0 para salir): "))
    
    if numero == 0:
        break
    suma += numero
print("La suma de los números ingresados es:", suma)
