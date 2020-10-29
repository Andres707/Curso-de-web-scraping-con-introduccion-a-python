__author__ = "Andres707"
'''
Las clases proveen una forma de empaquetar datos y funcionalidad juntos. Al crear una nueva clase, se crea un nuevo 
tipo de objeto, permitiendo crear nuevas instancias de ese tipo. Cada instancia de clase puede tener atributos adjuntos 
para mantener su estado. Las instancias de clase también pueden tener métodos (definidos por su clase) para modificar su estado.

Comparado con otros lenguajes de programación, el mecanismo de clases de Python agrega clases con un mínimo de nuevas 
sintaxis y semánticas. Es una mezcla de los mecanismos de clases encontrados en C++ y Modula-3. Las clases de Python 
proveen todas las características normales de la Programación Orientada a Objetos: el mecanismo de la herencia de clases 
permite múltiples clases base, una clase derivada puede sobre escribir cualquier método de su(s) clase(s) base, y 
un método puede llamar al método de la clase base con el mismo nombre. Los objetos pueden tener una cantidad arbitraria
de datos de cualquier tipo. Igual que con los módulos, las clases participan de la naturaleza dinámica de Python: 
se crean en tiempo de ejecución, y pueden modificarse luego de la creación.
'''
import random
import pandas as pd


class miprimerclase():
    def __init__(self):
        self.lis = []
        self.df = 0
        print('funcion principal')
        x = self.creacionListas(10)
        y = self.creacionListas(10)
        z = self.creacionListas(10)
        self.lista(x, 'y')
        self.listca(y, 'x')
        self.lista(z, 'z')
        print(self.lis)
        dicc = self.diccionario(self.lis)
        self.creacionDF(dicc)
        print(self.df)

    def creacionListas(self, numero):
        x = [i for i in range(numero)]
        random.shuffle(x)
        return x

    def creacionDF(self, lista):
        self.df = pd.DataFrame(lista)

    def lista(self, x, nom):
        self.lis.append([nom, x])

    def diccionario(self, lista):
        dc = dict(lista)
        return dc


if __name__ == '__main__':
    miprimerclase()
