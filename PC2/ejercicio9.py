'''
Al enviar mensajes de texto o twittear, no es raro acortar las palabras para ahorrar tiempo o espacio,
por ejemplo, omitiendo las vocales.
Implemente un programa que solicite al usuario una cadena de texto y luego retorne ese mismo
texto pero con todas las vocales (A, E, I, O y U) omitidas, ya sea que se ingresen en mayúsculas o
minúsculas.
Ejemplo:
- Input: Twitter Output: Twttr
- Input: What's your name? Output: Wht's yr nm?

'''

def omitir_vocales(cadena):
    
    resultado = ""

    for character in cadena:
        
        if character.lower() not in 'aeiou':
            resultado += character  

    return resultado

#le pedimos que ingrese un texto cualquiera 
texto = input("Ingrese una cadena de texto: ")


texto_sin_vocales = omitir_vocales(texto)


print(f'Texto con las vocales omitidas: {texto_sin_vocales}')
