from typing import List, Any, Union

texto = "Bello es mejor que feo." \
        " Explícito es mejor que implícito." \
        " Simple es mejor que complejo." \
        " Complejo es mejor que complicado." \
        " Plano es mejor que anidado." \
        " Espaciado es mejor que denso." \
        " La legibilidad es importante." \
        " Los casos especiales no son lo suficientemente especiales como para romper las reglas." \
        " Sin embargo la practicidad le gana a la pureza." \
        " Los errores nunca deberían pasar silenciosamente." \
        " A menos que se silencien explícitamente." \
        " Frente a la ambigüedad, evitar la tentación de adivinar." \
        " Debería haber una, y preferiblemente solo una, manera obvia de hacerlo." \
        " A pesar de que esa manera no sea obvia a menos que seas Holandés." \
        " Ahora es mejor que nunca." \
        " A pesar de que nunca es muchas veces mejor que *ahora* mismo." \
        " Si la implementación es difícil de explicar, es una mala idea." \
        " Si la implementación es fácil de explicar, puede que sea una buena idea." \
        " Los espacios de nombres son una gran idea, ¡tengamos más de esos!"

print(texto)
print('numero de caracteres {}'.format(len(texto)))
lista = texto.split()
print('numero de palabras {}'.format(len(lista)))


def conteoEspacios(cadena):
    contador = 0
    for i in range(len(cadena)):
        if cadena[i] == ' ':
            contador += 1
    return contador


print('Espacios: {}'.format(conteoEspacios(texto)))

print('palabra explicar {}'.format('explicar' in texto))

print('conteo de repeticones {}'.format(texto.count('que')))


def repeticones(texto, lista):
    sinduplicados = list(dict.fromkeys(lista))
    numdup = []
    for i in range(len(sinduplicados)):
        numdup.append([texto.count(sinduplicados[i]), sinduplicados[i]])
    numdup.sort(reverse=True)
    return numdup


x = repeticones(texto, lista)
for i in range(5):
    print(x[i])

def conteoPalabras(cadena):
    contador = 0
    for i in range(len(cadena)):
        if len(cadena[i]) >= 2:
                contador += 1
    return contador

print(conteoPalabras(lista))