a=1
ama=1500
mol=1000
bag=2000
inter=3000

pan=[0,1,2,3,4]
#Variables

while a==1:
    print('Amasao depana a $1500c/u mi reina[1]\nMolde depana a $1000c/u mi rei[2]\nBaguette wiwi $2000c/u Mon Roi [3]\nIntegral a $3000c/u pa los reales [4]\nSalir [5]')
    op=int(input('Seleccione una opcion : '))
    try:
        if 0 < op < 6 :
            if op==1:
                cant=input(print('Ha seleccionado Pan Amasado\nCuánto quiere comprar?  : '))
                pan.insert(0,cant)
                print(f'{cant} a un total de {cant*ama}')
                cont=int(input('Desea comprar otro tipo de pan? 1=SI 2=NO : '))
                if cont==1 :
                    print('bye bye')
                    a=0
            elif op==2:
                cant=input(print('Ha seleccionado Pan de Molde\nCuánto quiere comprar? : '))
                pan.insert(1,cant)
                print(f'{cant} a un total de {cant*mol}')
                cont=int(input('Desea comprar otro tipo de pan? 1=SI 2=NO : '))
                if cont == 1:
                    print('bye bye')
                    a=0
            elif op==3:
                cant=input(print('Ha seleccionado Pain baguette\nCombien voulez-vous acheter? : '))
                pan.insert(2,cant)
                print(f'{cant} a un total de {cant*bag}')
                cont = int(input('Desea comprar otro tipo de pan? 1=SI 2=NO : '))
                if cont == 1:
                    print('bye bye')
                    a=0
            elif op==4:
                cant=input(print('Ha seleccionado Pan Integral\nCuánto quiere comprar? : '))
                pan.insert(3,cant)
                print(f'{cant} a un total de {cant*inter}')
                cont = int(input('Desea comprar otro tipo de pan? 1=SI 2=NO : '))
                if cont == 1:
                    print('bye bye')
                    a=0
            else :
                print('Usted desea salir del menu')
                print('Hasta luego')
                a=0
        else:
            print('Ingresa una opcion valida porfa\n')
    except(ValueError):
        print('Ingrese un valor valido porfa\n')
    except(TypeError):
        print('Ingresa un tipo valido porfa\n')
    

#Resultados