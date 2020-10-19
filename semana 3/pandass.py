__author__ = "Andres707"
'''
pip install pandas
'''
import os
import pandas as pd
from random import shuffle
# creacion del dataframe
texto = ['Hola', 'a', 'todos', 'esta', 'es', 'una', 'prueba']
x = [i for i in range(len(texto))]
y = [i for i in range(len(texto))]
shuffle(x)
shuffle(y)


df = pd.DataFrame({'texto': texto, 'x': x, 'y': y})
print(df)

os.system('mkdir datos')
df.to_csv('datos/datos.csv', header=True, index=False)