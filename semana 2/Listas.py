__author__ = "Andres707"
'''
Como se crea una lista
nombre de la lista = [contenido separado por comas]
'''
#              0       1        2          3          4
palabras = ['rango', 'mapa', 'ocupar', 'dentista', 'entero']
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5]

# TODO: metodos de lista
# navegación dentro de la lista
print(palabras[3])
# [n:n] regresa el rango que este definido
print(palabras[0:2])
# cambiar un dato
palabras[2] = 'libre'
print(palabras)
# del funciona para eliminar en registro en concreto
del palabras[2]
print(palabras)
# Len funciona de la misma manera que en las cadenas
print(len(palabras))
# * n duplica la lista el numero de veces que le digamos
print(numeros * 2)
# TODO: Eliminar
# .remove Elimina una dato en concreto y elimina el primer dato que encuentra
numeros.remove(9)
print(numeros)
# dict.fromkeys elimina los dupliicados
num = list(dict.fromkeys(numeros))
print(num)
