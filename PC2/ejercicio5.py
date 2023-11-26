'''
Genere una función que tenga como parámetros el ingreso de un número entero y un dígito.
Verifique la cantidad de veces que se usa dicho número en el dígito solicitado.
Ejemplo:
Número ingresado: 15789000 y Dígito: 0
Cantidad de veces 0 en el número: 4

'''
def contar_digitos(numero, digito):
    
    numero_str = str(numero)      #para que me sea más facil operar, convierto de numero a srt 
    
    conteo = 0
    
    for d in numero_str:
        if d == str(digito):
            conteo += 1
    
    return conteo

# preguntamos numero a analizar y digito a contabilizar
numero_ingresado = int(input("introduca el numero a analizar: "))
digito_evaluar = int(input("que digito desea contabilizar:"))
cantidad = contar_digitos(numero_ingresado, digito_evaluar)

print(f"Cantidad de veces {digito_evaluar} en el número: {cantidad}")


