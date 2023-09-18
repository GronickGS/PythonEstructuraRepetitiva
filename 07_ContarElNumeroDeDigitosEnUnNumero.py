numero = int(input("Ingrese un número entero: "))
contador = 0
while numero != 0:
    numero //= 10
    contador += 1
print("El número tiene", contador, "dígitos.")
