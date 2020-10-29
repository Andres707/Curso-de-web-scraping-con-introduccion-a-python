from bs4 import BeautifulSoup
import requests
import pandas as pd
from time import sleep


class bot:
    def __init__(self):
        self.page = 0
        self.conjunto = list()
        self.lista = [['nombre', list()]]
        for i in range(1, 85, 1):
            if i < 10:
                url = 'https://www.uaeh.edu.mx/covid-19/mapa/municipio.php?m=' + '0' + str(i)
            else:
                url = 'https://www.uaeh.edu.mx/covid-19/mapa/municipio.php?m=' + str(i)
            headers = {'user-agent': 'my-app/0.0.1'}
            self.consulta(url, headers)
            self.estado()
            self.conjuntos()
            h1 = self.busqueda('h1')
            print(h1)
            th = self.busqueda('th')
            print(th)
            td = self.busqueda('td')
            print(td)
            del th[4]
            if i == 1:
                self.union(th)
            self.datos(td, h1)
            print(self.lista)
            sleep(15)
        dicc = self.creaciondic()
        self.creacion_csv(dicc)

    def creacion_csv(self, dicc):
        df = pd.DataFrame(dicc)
        df.to_csv('datos/covidHidalgoCompleto.csv', header=True, index=False)

    def creaciondic(self):
        return dict(self.lista)

    def union(self, th):
        for x in th:
            self.lista.append([x.text, list()])

    def datos(self, td, h1):
        for i in range(0, int(len(self.lista)), 1):
            if i == 0:
                for a in h1:
                    self.lista[i][1].append(a.text)
            else:
                for x in td[i - 1]:
                    self.lista[i][1].append(x)

    def consulta(self, url, headers):
        self.page = requests.get(url, headers=headers)

    def estado(self):
        estado = self.page.status_code
        print(estado)
        return estado

    def conjuntos(self):
        self.conjunto = BeautifulSoup(self.page.content, 'html.parser')

    def busqueda(self, dato):
        return self.conjunto.find_all(dato)


if __name__ == '__main__':
    bot()
