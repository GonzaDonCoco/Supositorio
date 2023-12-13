import numpy as np
import datetime

# Definir precios y rangos de asientos
PRECIOS = {'Platinum': 120000, 'Gold': 80000, 'Silver': 50000}
ASIENTOS_PLATINUM = list(range(1, 21))
ASIENTOS_GOLD = list(range(21, 51))
ASIENTOS_SILVER = list(range(51, 101))

# Arreglos para almacenar la información
asientos_disponibles = np.full((10, 10), 'O', dtype=str)
lista_asistentes = []

def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Comprar entradas")
    print("2. Mostrar ubicaciones disponibles")
    print("3. Ver listado de asistentes")
    print("4. Mostrar ganancias totales")
    print("5. Salir")

def comprar_entradas():
    global asientos_disponibles, lista_asistentes

    try:
        cantidad_entradas = int(input("Ingrese la cantidad de entradas (1-3): "))
        if cantidad_entradas < 1 or cantidad_entradas > 3:
            print("La cantidad de entradas debe estar entre 1 y 3.")
            return

        tipo_entrada = input("Ingrese el tipo de entrada (Platinum/Gold/Silver): ")
        if tipo_entrada not in PRECIOS:
            print("Tipo de entrada no válido.")
            return

        asientos_disponibles = mostrar_estado_venta()
        
        for _ in range(cantidad_entradas):
            fila, columna = seleccionar_asiento()
            if asientos_disponibles[fila, columna] == 'X':
                print("¡Ubicación no disponible!")
                return

            run_asistente = input("Ingrese el RUN del asistente (sin puntos ni guiones): ")
            if not validar_run(run_asistente):
                print("RUN no válido.")
                return

            # Registrar asistente
            lista_asistentes.append({
                'run': run_asistente,
                'tipo_entrada': tipo_entrada,
                'asiento': (fila, columna),
                'precio': PRECIOS[tipo_entrada]
            })

            # Marcar asiento como vendido
            asientos_disponibles[fila, columna] = 'X'

        print("Operación realizada correctamente.")

    except ValueError:
        print("Error: Ingrese un número válido para la cantidad de entradas.")

def mostrar_estado_venta():
    print("\n--- Estado de Venta ---")
    print(" 'O': Disponible")
    print(" 'X': Vendido")
    print("-----------------------")
    print(asientos_disponibles)
    return asientos_disponibles

def seleccionar_asiento():
    while True:
        try:
            fila = int(input("Ingrese la fila del asiento (1-10): "))-1
            columna = int(input("Ingrese la columna del asiento (1-10): "))-1

            if 0 <= fila < 10 and 0 <= columna < 10:
                
                return fila, columna
            else:
                print("Ubicación no válida. Ingrese valores dentro del rango.")
        except ValueError:
            print("Error: Ingrese números enteros para la fila y la columna.")

def ver_listado_asistentes():
    print("\n--- Listado de Asistentes ---")
    lista_asistentes_ordenada = sorted(lista_asistentes, key=lambda x: x['run'])
    for asistente in lista_asistentes_ordenada:
        print(f"RUN: {asistente['run']}, Tipo de entrada: {asistente['tipo_entrada']}, Asiento: {asistente['asiento']}, Precio: {asistente['precio']}")

def mostrar_ganancias_totales():
    total_ganancias = sum(asistente['precio'] for asistente in lista_asistentes)
    print(f"\nGanancias totales: ${total_ganancias}")

def validar_run(run):
    return run.isdigit() and len(run) == 9

def salida_sistema():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n¡Hasta luego, {nombre} {apellido}! Salida del sistema: {fecha_actual}")

# Menú principal
while True:
    mostrar_menu()
    opcion = input("Ingrese la opción deseada: ")

    if opcion == '1':
        comprar_entradas()
    elif opcion == '2':
        mostrar_estado_venta()
    elif opcion == '3':
        ver_listado_asistentes()
    elif opcion == '4':
        mostrar_ganancias_totales()
    elif opcion == '5':
        salida_sistema()
        break
    else:
        print("Opción no válida. Por favor, ingrese una opción válida.")
