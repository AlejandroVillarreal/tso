import numpy as np
from numpy.core.fromnumeric import size
import pandas as pd
import sys
data = {"n": [],
        "W": []}
#Variables
num_articulos = int(sys.argv[1])
v_min = int(sys.argv[2])
v_max = int(sys.argv[3])
w_min = int(sys.argv[4])
w_max = int(sys.argv[5])
num_instancias = int(sys.argv[6])
alpha = 0.3
W = int(((w_min + w_max)/2)*num_articulos*alpha)

#Generador de instancias
for instancia in range(num_instancias):

    dataframe = pd.DataFrame({ "n":[num_articulos],
                                "w":[W]})

    dataframe2 = pd.DataFrame({ "n":[np.random.randint(v_min,v_max) for _ in range(num_articulos) ],
                                "w":[np.random.randint(w_min,w_max) for _ in range(num_articulos)]})

    dataframe = dataframe.append(dataframe2)

    np.savetxt(r"C:\Users\alex_\Documents\9SEM\TEMAS_SELECTOS_OPTIMIZACION\Hw2\dataframes\instancia"+ str(instancia) + ".txt", dataframe, fmt="%d")

    print(dataframe)