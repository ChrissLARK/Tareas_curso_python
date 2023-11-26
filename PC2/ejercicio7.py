'''

Escriba una función de Python que tome un número como parámetro y verifique que el número sea
primo o no.


'''

def es_primo(numero):
    if numero <= 1:
        return False  
    
    # por definicion de primos buscamos si es divisible en un rango de  2 y la raíz cuadrada del número
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False  
    
    return True  

# Ejemplo de uso
numero = int(input("introduzca cualquier numero entero: "))
if es_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")


