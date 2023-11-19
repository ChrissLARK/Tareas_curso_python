'''
Escribir un programa que solicite al usuario que ingrese cuántos shows musicales ha visto en el
último año y almacene ese número en una variable. A continuación, mostrar en pantalla un valor de
verdad (True o False - tipo de datos booleanos) que indique si el usuario ha visto más de 3 shows

'''


# solicitamos cantidad de shows musicales vistos en el último año
shows_vistos = int(input("Ingresa la cantidad de shows musicales vistos en el último año: "))

# 
ha_visto_mas_de_3 = shows_vistos > 3

# motramos el valor booleano
print(f"¿Ha visto más de 3 shows musicales? {ha_visto_mas_de_3}")


