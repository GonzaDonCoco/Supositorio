#Ejercicio guia 4 arreglos
import random as r
import numpy as np

#Crear un arreglo unidimensional de largo 10 con numeros random y luego ingresar un numero y verificar si se encuentra en el arreglo
def ejercicio_1():
    arreglo= [r.randint(1,100) for i in range(10)]

    print(arreglo)

    numero=int(input('Ingrese el numero a buscar en el arreglo'))

    if numero in arreglo:
        print(f'El numero {numero} se encuentra en el arreglo en la posicion {arreglo.index(numero)}')
    else:
        print(f'El numero {numero} no se encuentra en el arreglo')

def ejercicio_2():
    filas=int(input('Ingrese un numero entre 3 y 6 (pueden ser ambos)'))
    columnas=int(input('Ingrese un numero entre 3 y 6 (pueden ser ambos)'))

    if 3<= filas <=6 and 3<=columnas <=6:
        arreglo = np.random.random(filas,columnas)
    else:
        print('chimbarongo')
    print(arreglo)

print('hola')
ejercicio_2