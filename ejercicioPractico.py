def pedir_nombre():
    while(True):
        nombre = input("Ingrese el nombre del estudiante: ")
        try:
            if(nombre):
                return nombre
            else:
                print("nombre invalido")
        except ValueError:
            print("nombre invalido")

def pedir_edad():
    while(True):
        try:
            edad = int(input("Ingrese la edad del estudiante: "))
            if edad > 0:
                return edad
            else:
                print("Edad debe ser mayor que 0")
        except ValueError:
            print("la edad es incorrecta")

def pedir_nota(numeroNota):
    while(True):
        nota = float(input("Ingrese la nota ",numeroNota," (0.0 a 5.0): "))
        if 0 <= nota <= 5:
            return nota
        else:
            print("la nota debe estar entre 0.0 y 5.0.")

def registrar_estudiante():
    print("\n---- Registro de estudiante ----")
    nombre = pedir_nombre()
    edad = pedir_edad()
    nota1 =  pedir_nota(1)
    nota2 = pedir_nota(2)
    nota3 = pedir_nota(3)

    return nombre, edad, nota1, nota2, nota3

def calcular_promedio(n1, n2, n3):
    promedio = (n1 + n2 + n3) / 3
    return promedio

def evaluar_estado(promedio):
    if promedio >= 4.0:
        return "Aprobado"
    elif promedio >= 3.0:
        return "En recuperacion"
    else:
        return "Reprobado"

def mostrar_estudiante(estudiante):
    print("\n----- Resultado del Estudiante -----")
    print(f"Nombre: {estudiante['nombre']}")
    print(f"Edad: {estudiante['edad']} años")
    print(f"Nota 1: {estudiante['nota1']:.2f}")
    print(f"Nota 2: {estudiante['nota2']:.2f}")
    print(f"Nota 3: {estudiante['nota3']:.2f}")
    print(f"Promedio: {estudiante['promedio']:.2f}")
    print(f"Estado académico: {estudiante['estado']}")

def mostrar_todos_los_estudiantes(lista_estudiantes):
    print("\n----- Listado de Estudiantes -----")

    if len(lista_estudiantes) == 0:
        print("No hay estudiantes registrados")
        return

    for i, estudiante in enumerate(lista_estudiantes, start=1):
        print(f"{i}. {estudiante['nombre']} - "f"Edad: {estudiante['edad']} - "f"Promedio: {estudiante['promedio']:.2f} - "f"Estado: {estudiante['estado']}")

def mostrar_resumen(lista_estudiantes):
    print("\n----- Resumen -----")
    total_estudiantes = len(lista_estudiantes)
    print("Total de estudiantes registrados: ",total_estudiantes)

    if total_estudiantes > 0:
        suma_promedios = 0
        for estudiante in lista_estudiantes:
            suma_promedios += estudiante["promedio"]

        promedio_general = suma_promedios / total_estudiantes
        print(f"Promedio general del grupo: {promedio_general:.2f}")
    else:
        print("Promedio general del grupo: 0.00")

def menu():
    print("\n----- SISTEMA DE GESTION BASICA DE ESTUDIANTES -----")
    print("1. Registrar estudiante")
    print("2. Mostrar todos los estudiantes")
    print("3. Salir")

estudiantes = []
while(True):
    menu()
    opcion = input("Seleccione una opción: ")
    match(opcion):
        case "1":
            nombre, edad, nota1, nota2, nota3 = registrar_estudiante()
            promedio = calcular_promedio(nota1, nota2, nota3)
            estado = evaluar_estado(promedio)

            estudiante = {
                "nombre": nombre,
                "edad": edad,
                "nota1": nota1,
                "nota2": nota2,
                "nota3": nota3,
                "promedio": promedio,
                "estado": estado
            }

            estudiantes.append(estudiante)
            mostrar_estudiante(estudiante)
        case "2":
            mostrar_todos_los_estudiantes(estudiantes)

        case "3":
            mostrar_resumen(estudiantes)
            print("Programa finalizado.")
            break

        case _:
            print("Opción no válida. Intente nuevamente.")
