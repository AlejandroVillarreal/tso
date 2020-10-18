import numpy as np
from numpy.core.fromnumeric import size
import pandas as pd
import sys

datos = pd.read_csv(r"instancia0.txt",sep=" ",names=["v","w"])





def quickSort(list):
    if not list:
        return list
    pivot = list[0]
    lesser = quickSort([x for x in list[0:] if x[0] < pivot[0]])
    greater = quickSort([x for x in list[0:] if x[0] >= pivot[0]])
    return lesser + [pivot] + greater


mochila = []

# Toma valor de la mochila indice 0 en columna w
capacidad = int(datos["w"].values[0])

peso_mochila = 0
# crea un nuevo dataframe sin el valor de la mochila y la cantidad de elementos
elementos = datos.iloc[1:]

#print(capacidad)
#print(elementos)
flag = 0;

#Ordena el dataframe segun los valores v de forma descendente
#v = elementos.sort_values("v",ascending=False)

#Transforma el dataframe a un array numpy
#array_elementos = v.to_numpy().tolist()

elementos = elementos.to_numpy()

#print(array_elementos)
def takeFirst(elem):
    return elem[0]
#array_elementos = sorted(elementos,key=takeFirst,reverse=True)
#Imprime el valor del inidice 0 osea el v del indice 0
#print(f"Elemento [0]: {array_elementos[0]}")
#array_elementos = quickSort(elementos)
sorted_elementos = -np.sort(-elementos)
array_elementos = sorted_elementos.tolist()

for elemento in array_elementos[:]:
    
    while(len(array_elementos) != 0 ):
        mejor_elemento = array_elementos[0]
        valor_mejor_elemento = array_elementos[0][0]
        #print(f"El mejor elemento: {mejor_elemento}")
        peso_mejor_elemento = array_elementos[0][1]
        #print(f"El peso del mejor elemento es: {peso_mejor_elemento}")
        if(int(peso_mejor_elemento) <= capacidad):
            
            mochila.append(array_elementos[0][0])
            #capacidad = capacidad - int(peso_mejor_elemento)
        #print(elementos[][])
        #array_elementos.remove(array_elementos.index(mejor_elemento))
            peso_mochila = peso_mochila + int(peso_mejor_elemento)
            capacidad = capacidad - int(peso_mejor_elemento)
            array_elementos.remove(mejor_elemento)
        else:
            array_elementos.clear()
        
        
        
        #else:
         #   pass
        #flag = 1
        
#print(f"El contenido de la mochila: {mochila}\n con un valor de: {sum(mochila)}\n con un peso de: {peso_mochila}")
print(f"X= {sum(mochila)}")
print(f"peso x: {peso_mochila}")
print("sorted")