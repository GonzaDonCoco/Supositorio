#Reto Python- Contraseña de 6 dígitos random
import re
import random as ra
import numpy as np


user_input=input()
patron = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net)"

if (re.search(patron,user_input)):
    print('Email válido')
else:
    print('Email inválido')

#Numeros de 1 a 1000 donde los pares printean "Fizz" e impares "Buzz"