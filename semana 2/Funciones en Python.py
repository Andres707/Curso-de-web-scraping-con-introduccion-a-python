__author__ = "Andres707"
'''
Funciones en Python
sintaxis
def():
    funciones
    return
'''


def conteo(cadena):
    return len(cadena)


def transformacion(cadena):
    return cadena.split()


def conteoEspacios(cadena):
    contador = 0
    for i in range(len(cadena)):
        if cadena[i] == ' ':
            contador += 1
    return contador


def main():
    texto = 'La frase "solo sé que no sé nada" ha estado sujeta a diferentes significados. Entre ellos, podemos destacar' \
            ' la sugerencia de que no existe la verdad absoluta, la constatación de los límites del conocimiento que ' \
            'podemos tener sobre las cosas, o la división que existe entre los sabios y los ignorantes.'
    numeroCaracteres = conteo(texto)
    print(numeroCaracteres)
    listaTexto = transformacion(texto)
    print(listaTexto)
    numeroPalabras = conteo(listaTexto)
    print(numeroPalabras)
    numeroEspacios = conteoEspacios(texto)
    print(numeroEspacios)


if __name__ == "__main__":
    main()
