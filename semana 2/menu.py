__author__ = "Andres707"
'''
Un pequeño menu
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
    menu = 'Menu \n' \
           '1. insertar texto \n' \
           '2. Conteo de caracteres \n' \
           '3. Transformacion a lista \n' \
           '4. Conteo de espacios \n' \
           '5. Fin'
    a = True
    texto = None
    while a:
        print(menu)
        opcion = int(input('inserta el numero que deseas: '))
        if opcion == 1:
            texto = input('inserta el texto: ')
        elif opcion == 2:
            if texto is not None:
                numeroCaracteres = conteo(texto)
                print('Numero de caracteres ', numeroCaracteres)
        elif opcion == 3:
            if texto is not None:
                listaTexto = transformacion(texto)
                print('Lista', listaTexto)
        elif opcion == 4:
            if texto is not None:
                numeroEspacios = conteoEspacios(texto)
                print('Numero de espacios ',numeroEspacios)
        elif opcion == 5:
            a = False
        else:
            print("opcion no valida")



if __name__ == "__main__":
    main()
