sw=False

menu=0

def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Ingresar informacion del empleado")
    print("2. Mostrar informacion de los empleados")
    print("5. Salir")

ano_ingreso=str
nombre=str
edad=int
genero={1:'Masculino',
        2:'Femenino',
        3:'No Binario'}
salario=float
fecha_ingreso=int

#Nombre, edad, genero, salario y fecha de ingreso
while not sw :
    mostrar_menu()
    menu=input('Ingrese su opcion: ')
    if menu==1:
        print('Ingrese la informacion del empleado:')
        nombre=input('Nombre de la persona: ')
        edad=input('Ingrese la edad:')
        genero=input('Ingrese el genero:\n[1]Masculino\n[2]Femenino\n[3]No Binario')
        salario=input('Ingrese el salario:')
        fecha_ingreso=input('Ingrese el año en que el empleado ingresa a la empresa: ')
    elif menu==2:
        print(f'Emplead@: {nombre}\nEdad:{edad}\nGenero:{genero}\nSalario:{salario}\nFecha de ingreso:{fecha_ingreso}')
    elif menu==5:
        print('CHIMBARONGO')
        break
    else:
        print('\nIngresa una huea buena')



