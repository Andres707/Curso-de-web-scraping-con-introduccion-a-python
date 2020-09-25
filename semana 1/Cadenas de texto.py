__author__ = "Andres707"

'''
Cadenas 
'''
saludo = 'Hola Mundo'
# TODO: Metodos de cadenas
# Strip se encarga de eliminar los caracteres que le demos
print(saludo.strip('Ho'))
# Count cuenta las veces que el caracter que le demos aparece dentro
# dentro de la lista
print(saludo.count('o'))
'''
Split particiona la cadena y la transforma  en una lista. 
tiene dos parametros que son opcionales
separator: la cada esta separada por '#' o ',' o hasta un numero
por defecto es el espacio
maxsplit: El numero maximo de divisiones que le dara a la cadena
'''
print(saludo.split())
'''
a = 'oau'
b = '123'
print(saludo.translate([a,b]))'''
# Index nos dice la posicion del caracter que estamos buscando
print(saludo.index('a'))
# .format nos ayuda a dar mensajes personalizados pueden ir basias las llaves o con un identificador
print('Hola {name}. Eres el numero {num}'.format(name='Andres', num=56))
# Find nos retorna la posición en la que inicia el valor que estamos buscando
print(saludo.find('do'))
'''
Center recibe dos parametros donde uno es obligatorio y el otro opcional
Length: Es la longitud que tendrá y pondrá en medio la cadena
Character: Es el caracter que pondra a los lados de la cadena
'''
print(saludo.center(20, '-'))
# .join Une os caracteres que le mandemos opcionalmete puedes darle el caracter que lo separa
saludo2 ='Hola a todos.'
saludo2 = saludo2.split()
print(saludo2)
x= '*'.join(saludo2)
print(x)