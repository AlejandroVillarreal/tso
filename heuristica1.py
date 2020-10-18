import numpy as np
from numpy.core.fromnumeric import size
import pandas as pd
import sys
#Variables
archivo = open(sys.argv[1])
datos = pd.read_csv(archivo,sep=" ",names=["v","w"])
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
v = elementos.sort_values("v",ascending=False)

#Transforma el dataframe a un array numpy
array_elementos = v.to_numpy().tolist()

#print(array_elementos)

#Imprime el valor del inidice 0 osea el v del indice 0
#print(f"Elemento [0]: {array_elementos[0]}")

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
        #else:
         #   pass
        #flag = 1
        
#print(f"El contenido de la mochila: {mochila}\n con un valor de: {sum(mochila)}\n con un peso de: {peso_mochila}")
print(f"X= {sum(mochila)}")
#print(capacidad)



        


