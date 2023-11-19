'''
Supongamos que estás en un país donde se acostumbra desayunar entre las 7:00 y las 8:00, almorzar
entre las 12:00 y las 13:00 y cenar entre las 18:00 y las 19:00.
Implemente un programa que solicite al usuario una hora y le indique si es la hora del desayuno, la
hora del almuerzo o la hora de la cena. Si no es hora de comer, no envíes nada.
Suponga que la entrada del usuario se formatea en formato de 24 horas como #:## o ##:##. Y
suponga que el rango de tiempo de cada comida es inclusivo. Por ejemplo, ya sean las 7:00, las 7:01,
las 7:59 o las 8:00, o en cualquier momento intermedio, es hora de desayunar.

'''


hora = input("Ingresa la hora en formato HH:MM (24 horas), por favor: ")

# usaré split para separar hora de minutos
hora_ingresada = hora.split(':')
hora= int(hora_ingresada[0])
minutos = int(hora_ingresada[1])

# Verificar si la hora ingresada corresponde a alguna comida
if 7 <= hora <= 8:
    print("Es hora de desayunar.")
elif 12 <= hora <= 13:
    print("Es hora de almorzar.")
elif 18 <= hora<= 19:
    print("Es hora de cenar.")
