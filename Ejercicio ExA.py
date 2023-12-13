#Ejercicios para el examen
import numpy as np
import datetime as dt

escenario=np.arange(1,101).reshape(10,10)
#print(escenario)

sw=True

def menu():
    print("\n--- Menú ---")
    print("1. Comprar entradas")
    print("2. Mostrar ubicaciones disponibles")
    print("3. Ver listado de asistentes")
    print("4. Mostrar ganancias totales")
    print("5. Salir")

def comprarEntradas():
    cantidad_entradas=int(input('Ingrese la cantidad de entradas a comprar 1-3: '))
    if cantidad_entradas


def asientosDisp():
    print('---Escenario---')
    print(escenario)
    print('----------------------------')

    

    
#def listAsistentes()
def salir():
    print('')
    print('¡Gracias por su preferencia!\nVuelva pronto')
    print('Programa desarrollado por: Gonzalo Peña O')
    print(f'Fecha y hora actuales: {dt.datetime.now().strftime("%d-%m-%Y")}')







while sw:
    try:
        menu()
        opcion=int(input('Ingrese una opción:\t'))
        if opcion!=5:
            if opcion==1:
                #Comprar entradas
                print('comprarEntradas()')
            elif opcion==2:
                #Mostrar asientos disponibles
                asientosDisp()
            elif opcion==3: 
                #Ver listado de asistentes
                print('listAsistentes')
            elif opcion==4:
                #Mostrar ganancias totales
                print('gananciaTotal()')
        else:
            salir()
            #sw=False
            break    

    except (ValueError):
        print('Ingrese un valor válido')
    except(TypeError):
        print('Ingrese una opción válida')