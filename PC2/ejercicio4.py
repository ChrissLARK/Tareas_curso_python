'''
Imaginemos que lo han contratado para un colegio donde se desea realizar un sistema por el cual se
pueda generar un listado de “n” alumnos y 3 calificaciones que corresponden a alguna de sus
materias.
Puede usar el siguiente esquema a manera de ejemplo
{
Alumno: Juan,
Notas: [10, 12, 15]
}
Una vez completado el ingreso de los datos, su programa debe mostrar en pantalla el listado
completo de los alumnos.

'''
#1ro definimos nombres y notas, para clocarlos en lista

def ingresar_calificaciones():
    alumno = input("Ingrese el nombre del alumno: ")
    nota1 = float(input("Ingrese la primera calificación: "))
    nota2 = float(input("Ingrese la segunda calificación: "))
    nota3 = float(input("Ingrese la tercera calificación: "))
    return {'Alumno': alumno, 'Notas': [nota1, nota2, nota3]}


def mostrar_listado(alumnos):
    print("Listado de alumnos y calificaciones:")
    for alumno in alumnos:
        print(alumno)

# evocamos una clumna vacia
alumnos = []

# para una cantidad n de alumnitos
num_alumnos = int(input("Ingrese el número de alumnos: "))

# Pedimos nombres y notas 

for i in range(num_alumnos):
    print(f"Ingrese los datos del alumno {i + 1}:")
    alumno = ingresar_calificaciones()
    alumnos.append(alumno)


mostrar_listado(alumnos)
