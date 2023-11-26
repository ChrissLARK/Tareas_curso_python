'''
Escriba un programa en Python para obtener la serie de Fibonacci entre 0 y 50.
Nota: La secuencia de Fibonacci es la serie de números:
0, 1, 1, 2, 3, 5, 8, 13, 21,. ...
Cada número siguiente se obtiene sumando los dos números anteriores.

'''

# definimos los 2 primeros terminos de las succion 
a, b = 0, 1


print(a)

# le colocamos la condición <50
while b <= 50:
    print(b)
    a, b = b, a + b

