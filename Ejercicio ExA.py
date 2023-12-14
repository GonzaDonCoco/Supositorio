#Ejercicio para el examen
import numpy as np
import datetime as dt

cancha=np.arange(1,101).reshape(10,10)
precios=np.array([['Platinum',120000,'Asientos del 1 al 20'],['Gold',80000,'Asientos del 21 al 50'],['Silver',50000,'Asientos del 51 al 100']])
#print(entradas)
asistentes=[]

def menu():
    print("\n--- Menú ---")
    print("1. Comprar entradas")
    print("2. Mostrar ubicaciones disponibles")
    print("3. Ver listado de asistentes")
    print("4. Mostrar ganancias totales")
    print("5. Salir")


        

def asientosDisp():
    print('---------------Escenario-----------------')
    print(cancha)
    print('-----------------------------------------')



def comprarEntradas():
    cantidad_entradas=int(input('Ingrese la cantidad de entradas a comprar 1-3: '))
    if 1<=cantidad_entradas<=3:
        for i in range(cantidad_entradas):
            asientosDisp()
            for n in precios:
                nombre_entrada, precio_entrada,tipo_entrada = n
                print(f'{nombre_entrada} por ${precio_entrada} ({tipo_entrada})')

            asiento=int(input('\nEscoga un asiento (1-100) :'))
            #verifica el asiento y lo reemplaza
            if asiento in cancha:
                posicion=np.where(cancha==asiento)
                cancha[posicion[0][0],posicion[1][0]]= 0
                
                rut=int(input('Ingrese su RUT sin puntos, guión ni dígito verificador :'))
                if validar_rut(rut):          
                    asistentes.append(rut)
                
                gananciaTotal(asiento)

                print(f'Tuki, Asiento {asiento} reservado\n')
                
            
            


def validar_rut(rut):
    if 7<= rut <=8 and rut.isdigit():
        return True

#def listAsistentes():

def gananciaTotal(asiento):
    platinum=0
    gold=0
    silver=0
    
    if 1<= asiento <=20:
        platinum+1
    elif 21<= asiento <=50:
        gold+1
    elif 51<=asiento<=100:
        silver+1

    print('Ganancias totales')
    print(f'Platinum    {platinum}entradas  Total: {platinum*precios[0,0]}') 
    #print(f'Gold    {gold}entradas  Total: {gold*precios[0,1]}')   


def salir():
    print('')
    print('¡Gracias por su preferencia!\nVuelva pronto')
    print('Programa desarrollado por: Gonzalo Peña O')
    print(f'Fecha y hora actuales: {dt.datetime.now().strftime("%d-%m-%Y")}')

comprarEntradas()


'''
#Menu del programa
sw=True
while sw:
    try:
        menu()
        opcion=int(input('Ingrese una opción:\t'))
        if opcion!=5:
            if opcion==1:
                #Comprar entradas
                comprarEntradas()
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
        print('Ingrese una opción válida')'''