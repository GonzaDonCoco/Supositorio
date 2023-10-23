tabla=[]
almacen=[]
tabla2=[]


while True:
    try:
        numero1=int(input('Ingrese un número para crear su tabla de multiplicación hasta 10 : '))
        if numero1!=0:
            break

    except(ValueError):
        print('Ingrese un número válido!')
    except(TypeError):
        print('Ingrese un valor válido!')

for i in range(11):
    if i==0:
        continue
    tabla.append(i*numero1)

print(tabla)

numero2=int(input('Ingrese números enteros de a uno para almacenarlos en una lista:\n Para terminar ingrese el "0" :'))
while numero2!=0:
    almacen.append(numero2)
    numero2=int(input('Ingrese otro numero\nPara salir "0"  '))

almacen.sort()
print(almacen)

for i in range(10):
    print('hola')