#ads

import numpy as np

'''Los precios de las entradas son los siguientes:
 Platinum, $120.000. (Asientos del 1 al 20).
 Gold, $80.000. (Asientos del 21 al 50).
 Silver, $50.000. (Asientos del 51 al 100.).'''

escenario=np.arange(1,101).reshape(10,10)
entradas=np.array([['Platinum',120000],['Gold',80000],['Silver',50000]])
run=input('papa')



print(escenario[1,1])
print('')
#Para convertir a entero y poder calcular
print(entradas[1,1].astype(int)*2)
if run.idigit() and run.len==9 :
    print('a')
else:
    print('b')



