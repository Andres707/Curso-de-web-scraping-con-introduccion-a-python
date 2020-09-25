__author__ = "Andres707"

'''
            Memoria
a = 564 -> [a=564]
b = 987 -> [b=987]
En python las variables no son ncesarias crearlas antes de usarlas
'''
# Asignacion de un valor a una variable
A = 56
b = 'Hola mundo'
c = 100101010101010

print(c)

# TODO: Variables globales

A = 103
def funcion():
    global A
    A = A + 10
    print('Este es el valor de A dentro de la funcion ', A)
print('Este es el valor de A fuera de la funcion ', A)
funcion()