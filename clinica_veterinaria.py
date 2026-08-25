import json

ARCHIVO = "clinica.json"

def inicializar_sistema():
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            json.load(f)
    except FileNotFoundError:
        datos = {
            "mascotas": [],
            "consultas": [],
            "vacunas": [],
            "documentos": []
        }
        with open(ARCHIVO, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4)

def cargar_datos():
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        return json.load(f)

def guardar_datos(datos):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)


def registrar_mascotas():
    datos = cargar_datos()

    print("\nREGISTRAR MASCOTAS:")
    codigo = input("Código: ")
    nombre = input("Nombre: ")
    especie = input("especie: ")
    raza = input("Raza: ")
    fecha_nacimiento = input("Fecha de nacimiento: ")
    nombre_propietario = input("nombre del propietario: ")
    while True:
        telefono_str = input("Ingrese el teléfono del propietario: ")
        if telefono_str.isdigit():
            telefono = int(telefono_str)
            break
        else:
            print("Precio no valido")
    while True:
        print("\nEstado : 1=activo | 2=inactivo): ")
        estado = input("Seleccione el estado de la mascota: ")
        if estado == "1":
            estado = "activo"
            break
        elif estado == "2":
            estado = "inactivo"
            break
        else:
            print("Estado no válido")

    registro = {
        "codigo": codigo,
        "nombre": nombre,
        "especie": especie,
        "raza": raza,
        "fecha_nacimiento": fecha_nacimiento,
        "nombre_propietario": nombre_propietario,
        "telefono": telefono,
        "estado": estado,
    }

    datos["mascotas"].append(registro)
    guardar_datos(datos)
    print("\nMascota registrada.")

def mostrar_catalogo(catalogo):
    datos = cargar_datos()
    print("\n--- MASCOTAS REGISTRADAS ---")
    if not datos["mascotas"]:
        print("No hay mascotas registradas.")
        return

    for m in datos:
        print(f"\nCódigo: {m['codigo']}")
        print(f"Nombre: {m['nombre']}")
        print(f"Género: {m['genero']}")
        print(f"Fecha de creación: {m['fecha_creacion']}")
        print(f"Precio: Q{m['precio']:.2f}")
        print(f"Disponible: {m['disponible']}")
        print(f"Plataformas: {m['plataformas']}")


def buscar_por_codigo(catalogo):
    datos = cargar_datos()
    print("\n--- BUSCAR POR MASCOTAS ---")
    codigo = input("Ingrese el código de la mascota: ")

    for m in datos["mascotas"]:
        if m["codigo"] == codigo:
            print(f"\nCódigo: {m['codigo']}")
            print(f"Nombre: {m['nombre']}")
            print(f"Especie: {m['especie']}")
            print(f"Raza: {m['raza']}")
            print(f"Fecha de nacimiento: {m['fecha_nacimiento']}")
            print(f"Propietario: {m['propietario']}")
            print(f"Teléfono: {m['telefono']}")
            print(f"Estado: {m['estado']}")
            return

    print("No se encontró ningúna mascota registrada.")


def registrar_consulta():
    datos = cargar_datos()
    print("\n--- REGISTRAR CONSULTA ---")
    codigo_consulta = input("Código de consulta: ")
    codigo_mascota = input("Código de mascota: ")
    fecha = input("Fecha: ")
    motivo = input("Motivo: ")
    diagnostico = input("Diagnóstico: ")
    tratamiento = input("Tratamiento: ")
    costo = float(input("Costo: "))

    consulta = {
        "codigo_consulta": codigo_consulta,
        "codigo_mascota": codigo_mascota,
        "fecha": fecha,
        "motivo": motivo,
        "diagnostico": diagnostico,
        "tratamiento": tratamiento,
        "costo": costo
    }



    datos["consultas"].append(consulta)
    guardar_datos(datos)
    print("\nConsulta registrada.")

def mostrar_por_plataforma(catalogo):
    print("\n--- BUSCAR POR PLATAFORMA ---")
    plataforma = input("Ingrese la plataforma: ").lower()

    for juego in catalogo:
        if plataforma in juego["plataformas"].lower():
            print(f"\nCódigo: {juego['codigo']}")
            print(f"Nombre: {juego['nombre']}")
            print(f"Plataformas: {juego['plataformas']}")


def calcular_precio_promedio(catalogo):
    print("\n--- PRECIO PROMEDIO ---")
    if not catalogo:
        print("El catálogo está vacío.")
        return

    total = 0
    for juego in catalogo:
        total += juego["precio"]

    promedio = total / len(catalogo)
    print(f"El precio promedio es: Q{promedio:.2f}")



inicializar_sistema()

while True:
    print("""\n  SISTEMA DE GESTIÓN DE CATÁLOGO 
    1. Registrar una mascota.
    2. Mostrar las mascotas registradas.
    3. Buscar una mascota por código.
    4. Registrar una consulta para una mascota.
    5. Consultar el historial de consultas de una mascota.
    6. Registrar una vacuna.
    7. Consultar las vacunas de una mascota.
    8. Asociar al menos un archivo externo a una mascota.
    9. Salir del programa.
    
    """)

    opcion = input("Seleccione una opción: ")

    match opcion:
        case "1":
            registrar_mascotas()
        case "2":
            continue
        case "9":
            print("\nSaliendo del programa...")
            break
        case _:
            print("Opción inválida.")