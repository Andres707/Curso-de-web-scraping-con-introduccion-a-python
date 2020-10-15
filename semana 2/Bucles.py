__author__ = "Andres707"
'''
Blucles en python 
WHILE
sintaxis
    contador = 0
    while contador < 18:
        contador += 1
FOR
sintaxis 
    for i in range(15):
        funcion 
'''
# while
contador = 0
while contador < 5:
    print('valor de contador: {}'.format(contador))
    print('Hola mundo')
    contador += 1
print()
# FOR
for i in range(5):
    print('Hola mundo')
print()
# saltos de dos en dos
# while
contador = 0
while contador < 5:
    print('valor de contador: {}'.format(contador))
    print('Hola mundo')
    contador += 2
print()
# FOR
# range(valor inicial, valor limite, numero de saltos)
for i in range(0, 5, 2):
    print('Hola mundo, valor de i: {}'.format(i))
print()
for i in 'Hola mundo':
    print(i)
print()
# 2 for`
listas = [[1, 2, 3, 5], [4, 5, 6, 8], [7, 8, 9, 0]]
for i in range(len(listas)):
    for j in range(len(listas[i])):
        print(listas[i][j])
print()
# 2 while
contador1 = 0
contador2 = 0
while contador1 < len(listas):
    while contador2 < len(listas[contador1]):
        print(listas[contador1][contador2])
        contador2 += 1
    contador1 += 1
    contador2 = 0
print('for')
# mixto
a = 0
for i in range(len(listas)):
    while True:
        if a == len(listas[i]):
            break
        print(listas[i][a])
        a += 1
    a = 0
