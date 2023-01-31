#Importando bibliotecas.
from bs4 import BeautifulSoup
import requests 

#Puxando o HTML do URL abaixo usando requests e jogando tudo na "sopa".
url = 'https://pt.wikipedia.org/wiki/Brasil'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

#Filtrando o HTML e puxando apenas os paragrafos <p> ('p').
texto_brasil = soup.find_all('p')

#Criando/editando um arquivo com o nome da variavel acima.
arquivo = open('texto_brasil.txt', 'w+', encoding="utf-8")
#Para cada paragrafo filtrado em texto_brasil, escreva o paragrafo em forma de texto no arquivo criado.
for t in texto_brasil:
  arquivo.write(t.text)

arquivo.close()

#Pedi pro davinci 003 otimizar o prototipo 0, esse foi o resultado com algumas correções de bugs. 
