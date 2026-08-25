import json
import os

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

    print("\n--- REGISTRAR MASCOTA ---")
    codigo = input("Código: ")
    nombre = input("Nombre: ")
    especie = input("Especie: ")
    raza = input("Raza: ")
    fecha_nacimiento = input("Fecha de nacimiento: ")
    nombre_propietario = input("Nombre del propietario: ")

    while True:
        telefono_str = input("Ingrese el teléfono del propietario: ")
        if telefono_str.isdigit():
            telefono = int(telefono_str)
            break
        else:
            print("Teléfono no válido. Ingrese solo números.")

    while True:
        print("\nEstado: 1 = activo | 2 = inactivo")
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
    print("\nMascota registrada exitosamente.")


def mostrar_mascotas():
    datos = cargar_datos()
    print("\n--- MASCOTAS REGISTRADAS ---")
    if not datos["mascotas"]:
        print("No hay mascotas registradas.")
        return

    for m in datos["mascotas"]:
        print(f"\nCódigo: {m['codigo']}")
        print(f"Nombre: {m['nombre']}")
        print(f"Especie: {m['especie']}")
        print(f"Propietario: {m['nombre_propietario']}")
        print(f"Teléfono: {m['telefono']}")
        print(f"Estado: {m['estado']}")


def buscar_por_codigo():
    datos = cargar_datos()
    print("\n--- BUSCAR MASCOTA ---")
    codigo = input("Ingrese el código de la mascota: ")

    for m in datos["mascotas"]:
        if m["codigo"] == codigo:
            print(f"\nCódigo: {m['codigo']}")
            print(f"Nombre: {m['nombre']}")
            print(f"Especie: {m['especie']}")
            print(f"Raza: {m['raza']}")
            print(f"Fecha de nacimiento: {m['fecha_nacimiento']}")
            print(f"Propietario: {m['nombre_propietario']}")
            print(f"Teléfono: {m['telefono']}")
            print(f"Estado: {m['estado']}")
            return

    print("No se encontró ninguna mascota registrada con ese código.")


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
    print("\nConsulta registrada exitosamente.")


def consultar_consulta():
    datos = cargar_datos()
    print("\n--- HISTORIAL DE CONSULTAS ---")
    codigo = input("Ingrese el código de la mascota a consultar: ")

    consultas_mascota = [c for c in datos["consultas"] if c.get("codigo_mascota") == codigo]

    if not consultas_mascota:
        print(f"No se encontraron consultas registradas para la mascota con código: {codigo}.")
        return

    for c in consultas_mascota:
        print(f"\nCódigo Consulta: {c['codigo_consulta']}")
        print(f"Fecha: {c['fecha']}")
        print(f"Motivo: {c['motivo']}")
        print(f"Diagnóstico: {c['diagnostico']}")
        print(f"Tratamiento: {c['tratamiento']}")
        print(f"Costo: Q{c['costo']:.2f}")


def registrar_vacuna():
    datos = cargar_datos()
    print("\n--- REGISTRAR VACUNA ---")
    codigo_mascota = input("Código de mascota: ")
    nombre_vacuna = input("Nombre de la vacuna: ")
    fecha_aplicacion = input("Fecha de aplicación: ")
    proxima_dosis = input("Próxima dosis: ")
    veterinario = input("Veterinario responsable: ")

    vacuna = {
        "codigo_mascota": codigo_mascota,
        "nombre_vacuna": nombre_vacuna,
        "fecha_aplicacion": fecha_aplicacion,
        "proxima_dosis": proxima_dosis,
        "veterinario": veterinario
    }

    datos["vacunas"].append(vacuna)
    guardar_datos(datos)
    print("\nVacuna registrada exitosamente.")


def consultar_vacunas():
    datos = cargar_datos()
    print("\n--- CONSULTAR VACUNAS ---")
    codigo = input("Ingrese el código de la mascota: ")

    vacunas_mascota = [v for v in datos["vacunas"] if v.get("codigo_mascota") == codigo]

    if not vacunas_mascota:
        print(f"No se encontraron vacunas registradas para la mascota con código: {codigo}.")
        return

    for v in vacunas_mascota:
        print(f"\nVacuna: {v['nombre_vacuna']}")
        print(f"Fecha de aplicación: {v['fecha_aplicacion']}")
        print(f"Próxima dosis: {v['proxima_dosis']}")
        print(f"Veterinario: {v['veterinario']}")


def asociar_documento():
    datos = cargar_datos()
    print("\nASOCIAR ARCHIVO EXTERNO ---")
    codigo = input("Ingrese el código de la mascota: ")

    print("\nArchivos detectados en la carpeta del programa:")

    archivos_locales = [f for f in os.listdir('.') if
                        os.path.isfile(f) and f not in ["clinica_veterinaria.py", "clinica.json"]]

    if not archivos_locales:
        print("  (No se detectaron archivos adicionales en esta carpeta)")
    else:
        for archivo in archivos_locales:
            print(f"  - {archivo}")

    nombre_documento = input("\nIngrese una descripción del documento (ej. Radiografía, Carnet): ")

    while True:
        nombre_archivo = input("Ingrese el nombre exacto del archivo de la lista anterior (ej. foto1.jpg): ")

        if os.path.exists(nombre_archivo):
            break
        else:
            print(f"Error: El archivo '{nombre_archivo}' no existe en la carpeta. Intente de nuevo.")

    documento = {
        "codigo_mascota": codigo,
        "nombre_documento": nombre_documento,
        "ruta_archivo": nombre_archivo
    }

    datos["documentos"].append(documento)
    guardar_datos(datos)
    print(f"\nDocumento '{nombre_archivo}' asociado exitosamente.")

inicializar_sistema()

while True:
    print("""\nSISTEMA DE GESTIÓN DE CATÁLOGO 
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

    opcion = input("\nSeleccione una opción: ")

    match opcion:
        case "1":
            registrar_mascotas()
        case "2":
            mostrar_mascotas()
        case "3":
            buscar_por_codigo()
        case "4":
            registrar_consulta()
        case "5":
            consultar_consulta()
        case "6":
            registrar_vacuna()
        case "7":
            consultar_vacunas()
        case "8":
            asociar_documento()
        case "9":
            print("\nSaliendo del programa...")
            break
        case _:
            print("Opción inválida. Por favor, intente de nuevo.")