#Reto Python- Contraseña de 6 dígitos random
import re
import random as ra
import numpy as np


"""def email():
    user_input=input()
    patron = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net)"

    if (re.search(patron,user_input)):
        print('Email válido')
    else:
        print('Email inválido')
"""
#Contraseña de 6 dígitos
def contraseñas():
    caracteres='abcdefghijklmnopqrstuvwxyz1234567890'
    contraseña=''

    for i in range (6):
        contraseña+=ra.choice(caracteres)
    print(contraseña)


#Numeros de 1 a 1000 donde los pares printean "Fizz", impares "Buzz" y primos "FizzBuzz"
def FizzBuzz():
    for i in range (1,1000):
        print(i)
        if i%2==0:
            print('Par')
        else:
            print('Impar')
        div = 0 
        for x in range(2,i):
            if(i%x==0):
                div+=1
        if(div==0):
            print("Primo")
        
            

            
FizzBuzz()
"""
#Otra forma de verificar el correo

def validar_correo_electronico(correo):
    # Patrón de expresión regular para validar direcciones de correo electrónico
    patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    # Comprobar si el correo cumple con el patrón
    if re.match(patron, correo):
        return True
    else:
        return False

# Ejemplo de uso
correo_ejemplo = input("ingrese el correo: ")

if validar_correo_electronico(correo_ejemplo):
    print(f"La dirección de correo electrónico {correo_ejemplo} es válida.")
else:
    print(f"La dirección de correo electrónico {correo_ejemplo} no es válida.")
"""