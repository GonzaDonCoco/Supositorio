#ads

import numpy as np

# Crear la matriz de la cancha
cancha = np.arange(1, 101).reshape(10, 10)

# Solicitar al usuario que elija un asiento
asiento = int(input('\nEscoja un asiento (1-100): '))

# Verificar si el asiento está en la cancha
if asiento in cancha:
    # Encontrar la posición del asiento
    posicion = np.where(cancha == asiento)

    # Mostrar la posición del asiento
    print(f"Posición del asiento {asiento}: Fila {posicion[0][0]}, Columna {posicion[1][0]}")

    # Reemplazar el asiento con un 0
    cancha[posicion[0][0], posicion[1][0]] = 0

    # Mostrar la matriz actualizada
    print("Matriz actualizada:")
    print(cancha)
else:
    print("El asiento no está en la cancha.")



