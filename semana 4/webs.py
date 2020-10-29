__author__ = "Andres707"
'''
pip install bs4
'''
from bs4 import BeautifulSoup
import requests
import os
import  pandas as pd
url = 'https://www.uaeh.edu.mx/covid-19/mapa/municipio.php?m=04'
headers = {'user-agent': 'my-app/0.0.1'}

page = requests.get(url, headers=headers)

print(page.status_code)

conjuntos = BeautifulSoup(page.content, 'html.parser')

# print(conjuntos)

PE = conjuntos.find_all('th')
print(PE)


TD = conjuntos.find_all('td')
print(TD)


t = conjuntos.find_all('h1')
print(t)
##-------------
print(PE[4])
del PE[4]
###-----------
listas = []

for x in t:
    listas.append(['nombre', x.text])

for y in PE:
    listas.append([y.text])
    #-1
for i in range(1, int(len(listas)), 1):
    for x in TD[i-1]:
        listas[i].append([x])
print(listas)
dicc = dict(listas)
print(dicc)
df = pd.DataFrame(dicc)
print(df)

os.system('mkdir datos')
df.to_csv('datos/covidHidalgo.csv', header=True, index=False)
