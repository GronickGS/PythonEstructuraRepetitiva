def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

n = int(input("Ingrese la cantidad de números primos a mostrar: "))
contador = 0
numero = 2
while contador < n:
    if es_primo(numero):
        print(numero)
        contador += 1
    numero += 1
