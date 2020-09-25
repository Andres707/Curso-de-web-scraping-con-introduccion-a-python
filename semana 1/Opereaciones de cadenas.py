__author__ = "Andres707"
'''
Operaciones de cadenas
'''

Texto = 'Existe un culto a la ignorancia. \n' \
        'La presión del anti-intelectualismo\n' \
        'ha ido abriéndose paso a través de \n' \
        'nuestra vida política y cultural. \n'
print(Texto)

# Len es una funcion que cuenta el numero de caracteres que tiene una cadena
print(len(Texto))
# Muestra una parte del texto
print(Texto[0:50])
# Invierte la cadena de texto
print(Texto[::-1])
print('\n')
# convierte la cadena en mayusculas
print(Texto.upper())
# convierte la cadena en minusculas
print(Texto.lower())