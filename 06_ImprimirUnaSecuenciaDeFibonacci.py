n = int(input("Ingrese la longitud de la secuencia de Fibonacci: "))

a, b = 0, 1
for i in range(n):
    print(a)
    a, b = b, a + b
