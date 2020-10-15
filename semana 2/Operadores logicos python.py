__author__ = "Andres707"
'''
Operadores logicos
'''
a = 6
b = 6
# Igualdad
if a is b:
    print("a es igual a b")
else:
    print("a no es igual a b")
print()
if a == b:
    print("a es igual a b")
else:
    print("a no es igual a b")
print()
# Diferencia
if a is not b:
    print("a no es igual a b")
else:
    print("a es igual a b")
print()
if a != b:
    print("a no es igual a b")
else:
    print("a es igual a b")
print()
# menor o mayor
if a < b:
    print('a menor que b')
else:
    print('a no es menor que b')
if a > b:
    print('a es mayor que b')
else:
    print('a no es mayor que b')
print()
# menor o igual y mayor o igual
if a <= b:
    print('a es menor o igual que b')
else:
    print('a no es menor ni igual que b')
if a >= b:
    print('a es mayor o igual que b')
else:
    print('a no es mayor ni igual que b')
print()
'''
AND
dos iguales verdaderos para tener un resultado verdadero 
'''
x = False
y = True
print('X y Y son ', x and y)
'''
OR
Solo necesita un valor verdadero para tener un resultado verdadero 
'''
print('X o Y son ', x or y)
'''
NOT
esta actúa como un inversor
'''
print('no de X ', not x)
print()
'''
in 
Verdadero si el valor / variable se encuentra en la secuencia
'''
C = [1, 2, 3]
A = 2
print('A esta en C: {}'.format(A in C))
print('A no esta en C: {}'.format(A not in C))

