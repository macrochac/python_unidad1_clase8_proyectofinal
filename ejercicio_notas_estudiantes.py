estudiantes = {}

#FUNCIÓN REGISTRO DE ESTUDIANTE
def registrar_estudiante():
    
    nombre = input("Ingrese el nombre del estudiante: ")
    
    while(True):
        edad = int(input("Ingrese la edad del estudiante: "))
        if edad <= 0:
            print("Dato mal ingresado! El dato debe ser positivo \n")
        else:
            break
    

    while(True):
        nota1 = float(input("Ingrese la nota número 1 del estudiante: "))
        nota2 = float(input("Ingrese la nota número 2 del estudiante: "))
        nota3 = float(input("Ingrese la nota número 3 del estudiante: "))
        if nota1 <= 5 and nota2 <= 5 and nota3 <= 5 and nota1>= 0 and nota2>= 0 and nota3>= 0 :
            break
        else:
            print("Dato mal ingresado! Las notas deben estar entre 0 y 5 \n")
    
    promedio = calcular_promedio(nota1,nota2,nota3)
    estado = evaluar_estado(promedio)
        
    estudiante = {
        'nombre'    :   nombre,
        'edad'      :   edad,
        'nota1'     :   nota1,
        'nota2'     :   nota2,
        'nota3'     :   nota3,
        'promedio'  :   promedio,
        'estado'    :   estado
        }
    
    estudiantes[nombre] = estudiante
    return estudiante


#FUNCIÓN CALCULO DEL PROMEDIO
def calcular_promedio(nota1, nota2, nota3):
    promedio = (nota1 + nota2 + nota3)/3
    return promedio


#FUNCIÓN EVALUAR ESTADO
def evaluar_estado(promedio):
    if promedio < 3.0 :
        return "Reprobado"
    elif promedio >= 3.0 and promedio < 4.0 :
        return "En recuperación"
    elif promedio >= 4.0:
        return "Aprobado"
    else:
        return "El dato del promedio es inválido"

#-----------------------PROGRAMA PRINCIPAL----------------------------------------

opciones = """Por favor seleccione una opción.
            1. Registrar estudiante
            2. Mostrar todos los estudiantes
            3. Salir
            Ingrese la opcion: """

opcion = 0
while opcion != 3:
    opcion = int(input(opciones))
    if opcion == 1:
        estudiante = registrar_estudiante()
        nota1 = estudiante['nota1']
        nota2 = estudiante['nota2']
        nota3 = estudiante['nota3']
        print("===== SISTEMA DE ESTUDIANTES =====")
        print(f"El estudiante {estudiante['nombre']} tiene:")
        print(f"Edad: {estudiante['edad']}")
        print(f"promedio: {estudiante['promedio']:.2f}")
        print(f"estado: {estudiante['estado']} \n")
    elif opcion == 2:
        if len(estudiantes)>0:
            print("Lista de estudiantes:")
            for idx, estudiante in enumerate(estudiantes.values()):
                print(f"""{idx+1}) nombre: {estudiante['nombre']}, edad: {estudiante['edad']}, promedio: {estudiante['promedio']:.2f}, estado: {estudiante['estado']} """)
        else:
            print("No hay estudiantes registrados")
    elif opcion == 3:
        suma_promedios = 0
        if len(estudiantes)>0:
            for estudiante in estudiantes.values():
                suma_promedios += estudiante['promedio']
            promedio_general = suma_promedios/len(estudiantes)
            print(f"El total de estudiantes registrados es: {len(estudiantes)}")
            print(f"El promedio general es: {promedio_general}")
        else:
            print("No hay estudiantes registrados")
        break

    else:
        print("Opción no valida, ingrese el dato de nuevo.")