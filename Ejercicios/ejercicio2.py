'''
1.-el programa preguntará al usuario, el valor de su consumo 
2.-luego pedirá información sobre el porcentaje que quiera dejar como propina
3.-Si coloca un % < 15, el programa advertirá al usiario a que coloque un porsentaje >= a 15% 
4.-El programa ejecutará los calculos y le brindará un resumen del total de la cuenta a pagar

'''
print('''Estimado cliente, por favor coloque el valor de su consumo:
       ''')

c=float(input("El valor de su consumo es: "))

print('''A continuación, por favor coloque el porcentaje que desea dejar al personal de atención al cliente \n 
      NOTA: el porcentaje debe ser igual o mayor al 15%
      ''')
p=float(input("Introduzca el porcentaje que desea dejar: "))

while p < 15:    #usé el while, lo vi en el libro que brindó, porque no se ocurria la manera de hacerlo con las condicionales
    print(f'el porcentaje que ingresó es menor al porcentaje mínimo de propina por favor, introduzca un porcentaje mayor o igual al minimo permitido')
    
    p=float(input("Introduzca el porcentaje que desea dejar: "))

h=c*(p/100)
t=c+(c*h)

print(f'\n\n A continuación le brindamos un resumen de la cuenta a pagar')
print(f'Su consumo fue de\t\t\t :{round(c,2)}')
print(f'La propina que dejará corresponde a\t:{round(h,2)}')
print(f'El total a pagar es\t\t\t:{round(t)}')

print(f'\n \n Gracias por su preferencia, vuelva pronto')
 
