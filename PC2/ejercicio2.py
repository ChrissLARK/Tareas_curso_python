'''
Escriba un programa en Python para construir el siguiente patrón.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*

'''


n = int(input("introduzca un numero que definira el tamaño del patron(será el numero de asteriscos de la fila más larga):  "))  #quize hacerlo mas bonito


for i in range(n):
    print('* ' * (i + 1))


for i in range(n - 1, 0, -1):
    print('* ' * i)

