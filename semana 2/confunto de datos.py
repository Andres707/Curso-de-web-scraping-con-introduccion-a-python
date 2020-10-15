__author__ = "Andres707"
'''
Un conjunto de datos es la colección de elementos desordenados, siendo cada elemento único.
ejemplo = {1,2}
'''
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8, 9}
print(type(conjunto2))

# Unión de dos conjuntos de datos dejando fuera los elementos repetidos
print('Unión de dos conjuntos de datos dejando fuera los elementos repetidos {}'.format(conjunto1 | conjunto2))
# Intersección de dos conjuntos de datos, regresa los elementos donde cruzan los dos
print('Intersección de dos conjuntos de datos, regresa los elementos donde cruzan los dos {}'.format(conjunto1 & conjunto2))
# Diferencia entre los conjuntos de datos
print('Diferencia entre los conjuntos de datos 1 y 2 {}'.format(conjunto1 - conjunto2))
print('Diferencia entre los conjuntos de datos 2 y 1 {}'.format(conjunto2 - conjunto1))
