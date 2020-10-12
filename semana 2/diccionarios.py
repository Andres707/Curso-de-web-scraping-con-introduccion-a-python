__author__ = "Andres707"
'''
Sintaxis de la creacion de un diccionario
nombre del diccionario:{nombre_clave: valor, nombre_clave1: valor,}
'''
alumnos = {
    1: {
        'nombre': 'Abigail Altúzar',
        'edad': 24
    },
    2: {
        'nombre': 'Paula Alejandra ',
        'edad': 29
    }
}
# Vista y forma de moverse dentro de un Diccionario
print(alumnos[2]['nombre'])
# Duplicar diccionario con .copy() sin dependencia
x = alumnos.copy()
print(x)
print("x es dependiente de alumnos ", x is alumnos)
# Duplicar diccionario con dependencia
y = alumnos
print(y)
print("y es dependiente de alumnos ", y is alumnos)
alumnos[3] = {
    'nombre': 'Oscar Gildardo ',
    'edad': 32}
print(y)
# Vaciar un diccionario con .clear()
print(len(alumnos))
alumnos.clear()
print(len(alumnos))
# dict()
dic = dict({1: {'nombre': 'Andres'}})
print(dic)
dic.clear()
# ZIP()
dic = dict(zip('abcde', [1, 2, 3, 4, 5]))
print(dic)
# items()
item = dic.items()
print(item)
# keys()
print(dic.keys())
# values()
print(dic.values())
# formkeys()
print(dic.fromkeys(['a', 'b'],1))
# get ()
print(dic.get('d'))
# pop()
print(dic.pop('b'))
print(dic)
