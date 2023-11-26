'''
Escribe una función de Python para calcular el factorial de un número (un entero no negativo). La
función acepta el número como argumento. 

'''

def factorial(numero):
    if numero < 0:
        return "No se puede calcular el factorial de un número negativo"
    elif numero == 0 or numero == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, numero + 1):
            resultado *= i
        return resultado

#ahora que calcule fact! del numero que introduzca el que use le programa. 

numero = int(input("introduzca un numero"))
fact = factorial(numero)
print(f"El factorial de {numero} es: {fact}")
