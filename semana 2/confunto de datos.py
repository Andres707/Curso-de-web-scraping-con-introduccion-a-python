__author__ = "Andres707"
'''
Un conjunto de datos es la colección de elementos desordenados, siendo cada elemento único.
ejemplo = {1,2}
'''
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8, 9}
print(type(conjunto2))

# Unión de dos conjuntos de datos dejando fuera los elementos repetidos
print(conjunto1 | conjunto2)
# Intersección de dos conjuntos de datos, regresa los elementos donde cruzan los dos
print(conjunto1 & conjunto2)
# Diferencia entre los conjuntos de datos
print(conjunto1 - conjunto2)
print(conjunto2 - conjunto1)
