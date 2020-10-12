__author__ = "Andres707"
'''
Operadores basicos en python
'''
a = 25
b = 2

# suma
c = a + b
print('La suma de a y b es: {} \n'.format(c))
# resta
c = a - b
print('La resta de a y b es: {}\n'.format(c))
# Multiplicacion
c = a * b
print('La multiplicacion de a por b es: {}\n'.format(c))
# Division
c = a / b
print('La division de a entre b es: {}\n'.format(c))
# Division entera
c = a // b
print('La division entera es: {}\n'.format(c))
# Modulo
c = a % b
print('El modulo de a entre b es: {}\n'.format(c))
# Exponente
c = a ** b
print('El exponente entre a y b es: {}\n'.format(c))
# Negacion
c = -b
print('El valor negativo de b es: {}\n'.format(c))
'''
Orden de precedencia
1.Exponente: **
2.Negación: -
3.Multiplicación, División, División entera, Módulo: *, /, //, %
4.Suma, Resta: +, -
'''
c = 2 ** 2 / 22
print('El resultado de la operacion 2^2/22 es: {}\n'.format(c))
c = 2 ** (2 / 22)
print('El resultado de la operacion saltandose el orden 2^(2/22) es: {}\n'.format(c))
#
d = 10
# suma el operador izquierdo al derecho
d += b
print('La suma es: {}\n'.format(d))
# resta el operador izquierdo al derecho
d = 10
d -= b
print('La suma es: {}\n'.format(d))
