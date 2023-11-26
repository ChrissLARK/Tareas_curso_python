'''
Por medio de un bucle While genere un código que permita el ingreso de números por teclado. El
ingreso de los números debe ser permitido hasta que el usuario decida ya no ingresar nuevos
números.
Con dichos números, su programa debe evaluar cada uno de estos números e indicar la cantidad de
números pares e impares.

'''
#lista y contadores 

numeros = []  
pares = 0  
impares = 0  

#configurando bucle 

continuar = True
while continuar:
    respuesta = input("Desea ingresar un número? (SI/NO): ").upper()
    
    if respuesta == "SI":
        numero = int(input("Ingrese el número: "))
        numeros.append(numero)  
        
        if numero % 2 == 0:
            pares += 1  
        else:
            impares += 1  
    elif respuesta == "NO":
        continuar = False  
    else:
        print("Por favor, responda con SI o NO.")


print(f"Números ingresados: {numeros}")
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
