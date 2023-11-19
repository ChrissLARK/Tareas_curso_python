'''
Escribir un programa que lea un entero positivo, N, introducido por el usuario y después muestre en
pantalla la suma de todos los enteros desde 1 hasta N. La suma de los N primeros enteros positivos
puede ser calculada de la siguiente forma: 

'''
'''pedimos un numero entero psitivo'''

numero = int(input("Ingresa un número entero positivo: "))

# Verificar si el número es positivo
if numero <= 0:
    print("Por favor, ingresa un número entero positivo.")
else:
    suma = 0

    # Calcular la suma de los enteros desde 1 hasta N
    for i in range(1,  numero+ 1):
        suma += i

    # Mostrar el resultado
    print(f"La suma de los primeros {numero} enteros positivos es: {suma}")