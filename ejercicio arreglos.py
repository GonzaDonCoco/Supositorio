#Ejercicios de arreglos tipo prueba 3
import numpy as np

lista = [[1, "", 1], [2, "", 2]]
array = np.array(lista)
print(array)


# Agregar
# Se solicitan los datos para ser ingresados al arreglo
def agregar():
    numPart = input("Ingrese numero de parte: ")
    if len(numPart) == 10:
        nomProd = input("Ingrese nombre parte: ")
        if len(nomProd) >= 6:
            precioProd = int(input("Ingrese precio parte: "))
            if precioProd > 0:
                # Se compilan los datos en un arreglo bidimensional para luego ser enviados al array
                dato = [[numPart, nomProd, precioProd]]
                # Usamos la palabra clave global para indicar que usaremos una variable que se encuentra fuera de la funcion
                global array
                # Usamos funcion append para agregar un dato al arreglo
                # np.append(Arreglo que usaremos,dato nuevo a ingresar,axis=0 para indicar que agregaremos en vertical)
                array = np.append(array, dato, axis=0)
            else:
                print("Precio debe ser mayor a 0")
        else:
            print("Nombre debe tener minimo 6 caracteres")
    else:
        print("Numero de parte debe tener largo 10")


def buscar(numeroParte):
    # Declaramos variable array global para usar la variable fuera de la funcion
    global array
    # Preparamos un ciclo for que recorra toda la estructura
    for dato in array:
        # Validamos que dato[0] sea igual al numero de parte entregado
        if dato[0] == numeroParte:
            # Validamos que el precio sea mayor a 500 para confirmar el stock
            if int(dato[2]) > 500:
                print(f"Numero de parte: {dato[0]}")
                print(f"Nombre parte: {dato[1]}")
                print(f"Precio parte: {dato[2]}")
            else:
                print("No hay Stock")
            return True

    return False


def listar():
    # Generamos variable array global para usar nuestro array externo
    global array
    # generamos un ciclo for para recorrer toda nuestra matriz
    for dato in array:
        # Imprimimos todo el registro existente
        print("--------------------------------------")
        print(f"Numero de parte: {dato[0]}")
        print(f"Nombre parte: {dato[1]}")
        print(f"Precio parte: {dato[2]}")
        print("-------------------------------------- \n")


opcion = 0
# Declaramos opcion para elegir en nuestro menu
# Generamos ciclo while con opcion !=4 para filtrar las opciones elegidas

while opcion != 4:
    # Realizamos un try except para controlar fallos de ingreso de valor
    try:
        print("Menu Principal")
        print("1.- Agregar parte")
        print("2.- Buscar parte")
        print("3.- Listar partes")
        print("4.- Salir")
        opcion = int(input("Ingrese opcion que desea: "))
        # Solicitamos opcion y filtramos segun opcion elegida
        # Dependiendo de la opcion generamos un filtro con condicion IF para decidir que funcion llamar
        if opcion == 1:
            agregar()
        elif opcion == 2:
            numPart = input("Ingrese numero de parte que desea buscar")
            buscar(numPart)
        elif opcion == 3:
            listar()
        elif opcion == 4:
            print("Gracias por su preferencia, Desarrollado por Jose Riquelme")
    except ValueError:
        print("Debe ingresar un numero")



