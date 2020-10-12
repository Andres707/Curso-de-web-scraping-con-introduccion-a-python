__author__ = "Andres707"
# TODO: tipo de numeros
# Entero
entero = 564
print(type(entero))
# Float
flotante = 10.65
print(type(flotante))
# complejos
# creacion directa
comple = 2e2j
print(comple)
print(type(comple))
# creacion apartir de complex
complejo = complex(2, 3)
print(complejo)

# TODO: casteos

print('Esta es la nueva clase de entero ', type(float(entero)), ' Este es el nuevo valor ', float(entero))

print('Esta es la nueva clase de flotante  ', type(int(flotante)), ' Este es el nuevo valor ', int(flotante))

print('Esta es la nueva clase de entero ', type(complex(entero)), ' Este es el nuevo valor ', complex(entero))

# meotodos
Texto = 'Binahria'
# texto con numero
print(entero, Texto)
# entero con float
print(entero+flotante)
# float con entero
print(flotante*entero)
# castear entero a string para concatenar texto
print(str(entero)+Texto)
print(entero, complejo)
# entero con float
print(entero+complejo)
print(entero*complejo)