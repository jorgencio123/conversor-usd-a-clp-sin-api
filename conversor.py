import requests
from bs4 import BeautifulSoup
import math

url = 'https://www.xe.com/es/currencyconverter/convert/?Amount=1&From=USD&To=CLP'
page = requests.get(url)
soup = BeautifulSoup (page.content , 'html.parser')

algo= soup.find_all('p' , class_='result__BigRate-sc-1bsijpp-1 iGrAod')

valor = list()
for i in algo:
    valor.append(i.text)

separado = valor.pop(0)
separado=separado.split()
separado=separado.pop(0)
separado=list(separado)
separado[3]="."
separado=''.join(separado)
separado=int(float(separado))
separado=round(separado)
print(separado) 

