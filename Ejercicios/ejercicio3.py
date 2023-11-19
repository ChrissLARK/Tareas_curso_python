'''
#Ejercicio 3 
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta
por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el
peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y
cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el
último pedido y calcule el peso total del paquete que será enviado.
'''
'''
    1.-El programa debera solicitar al cliente el # de payasos y muñecas 
    2.-Se calculará el peso total del pedido
    3.-El programa, dará un resumen del pedido y su peso 
'''
pedidos_payasos=int(input("Introduzca la cantidad de payasos que ha pedido"))
pedidos_muniecas=int(input("Introduzca la cantidad de muñecas que ha pedido"))

peso_payasos_g=pedidos_payasos*112
peso_muniecas_g=pedidos_muniecas*75

peso_payasos_kg=peso_payasos_g/1000
peso_muniecas_kg=peso_muniecas_g/1000

peso_total=peso_payasos_kg+peso_muniecas_kg

print(f'A continuación detallaremos su pedido y el peso total del mismo\n\n\n')

print(f'Cantidad de payasos pedidos\t:{pedidos_payasos}\t Peso en kg\t:{round(peso_payasos_kg,2)}')

print(f'Cantidad de muñecas pedidos\t:{pedidos_muniecas}\t Peso en kg\t:{round(peso_muniecas_kg,2)}')

print(f'\n\nEl peso total de su pedido en kg es \t :{round(peso_total,2)}')
      
print("\n\n\n ... Fin del programa ...")