#Ejercicio guia 4 arreglos
import random as r
import numpy as np

def menu():
    print('------------------')
    print('Menu Simple')
    print('[1]-Ejercicio 1')
    print('[2]-Ejercicio 2')
    print('[3]-Ejercicio 3')
    print('[8] Para salir')
    print('------------------')


def ejercicio_1():
    #Crear un arreglo unidimensional de largo 10 con numeros random y luego ingresar un numero y verificar si se encuentra en el arreglo
    arreglo= [r.randint(1,100) for i in range(10)]

    print(f'El arreglo es = {arreglo}')

    numero=int(input('Ingrese el numero a buscar en el arreglo'))

    if numero in arreglo:
        print(f'El numero {numero} se encuentra en el arreglo en la posicion {arreglo.index(numero)}')
    else:
        print(f'El numero {numero} no se encuentra en el arreglo')

def ejercicio_2():
    filas=int(input('Ingrese un numero entre 3 y 6 (pueden ser ambos)'))
    columnas=int(input('Ingrese un numero entre 3 y 6 (pueden ser ambos)'))

    if 3<= filas <=6 and 3<= columnas <=6:
        arreglo = np.random.randint(1, 100, size=(filas, columnas))
        suma_arreglos=np.sum(arreglo, axis=1)
        promedio_arreglos=np.mean(arreglo,axis=0)
        print('El arreglo es\n',arreglo)
        print('\n Suma por filas =',suma_arreglos)
        print('\n El promedio por columnas =',promedio_arreglos)
    else:
        print('chimbarongo')
    

#def ejercicio_3():



opcion=0
while opcion!=8:
    menu()
    try:
        opcion=int(input('Ingrese una opcion'))
        if opcion==1:
            ejercicio_1()
        elif opcion==2:
            ejercicio_2()
        elif opcion==8:
            print('Hasta luego')

    except ValueError:
        print("Debe ingresar un numero")
