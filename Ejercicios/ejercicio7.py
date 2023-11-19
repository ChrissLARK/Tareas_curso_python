'''
Realiza un programa que lea dos números por teclado y permite elegir entre 3 opciones en un menú:
- Mostrar una suma de los dos números
- Mostrar una resta de los dos números (el primero menos el segundo)
- Mostrar una multiplicación de los dos números
- En caso de introducir una opción inválida, el programa informará de que no es correcta.

'''



# Función para mostrar el menú y obtener la opción del usuario
def mostrar_menu():
    print("¿Qué operación quieres realizar?")
    print("1. Mostrar suma de los dos números")
    print("2. Mostrar resta (primer número menos segundo número)")
    print("3. Mostrar multiplicación de los dos números")
    opcion = input("Elige una opción (1/2/3): ")
    return opcion

# Función para realizar la operación seleccionada
def realizar_operacion(opcion, num1, num2):
    if opcion == '1':
        resultado = num1 + num2
        print(f"La suma de {num1} y {num2} es: {resultado}")
    elif opcion == '2':
        resultado = num1 - num2
        print(f"La resta de {num1} menos {num2} es: {resultado}")
    elif opcion == '3':
        resultado = num1 * num2
        print(f"La multiplicación de {num1} y {num2} es: {resultado}")
    else:
        print("Opción inválida")

# Pedir al usuario que ingrese dos números
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

# Mostrar el menú y realizar la operación seleccionada
opcion_elegida = mostrar_menu()
realizar_operacion(opcion_elegida, numero1, numero2)

