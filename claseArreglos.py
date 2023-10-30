import numpy as np

#Arreglo unidimensional de tamaño 10 con elementos aleatorios enteros del 0 al 100
arreglo1=np.random.randint(100, size=10)
print(arreglo1)


#copiar arreglo
arreglo2=arreglo1
#mayor
print('Elemento mayor')
print(arreglo2.max())
print('**************')
#menor
print('Elemento menor')
print(arreglo2.min())
print('**************')
#suma
print('Suma de elementos')
print(arreglo2.sum())
print('**************')
#promedio
print('Promedio de los elementos')
print(arreglo2.mean())
print('**************')
#Mostrar todos los elementos
print('Mostrar todos los elementos')
print(arreglo2)





