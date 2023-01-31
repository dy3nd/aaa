#Esse codigo foi feito com a ajuda do model "davinci 003", as bibliotecas foram ideia dele :)

import requests
from bs4 import BeautifulSoup

#definir o User, se não o request não funciona. Esse é o user padrão do Chrome.
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.120 Safari/537.36'}

#Faz a chamada da pagina web abaixo usando a library "requests"
page = requests.get("https://pt.wikipedia.org/wiki/Brasil",headers=headers)

#Analisa a variavel page(que fez o request), usando o html parser da library "Beautiful Soup"
soup = BeautifulSoup(page.content, 'html.parser')

#Filtra o HTML da pagina com esses 2 parametros (div e o nome da class)
filtro_divs = soup.find_all("div", class_="mw-parser-output")

#Define uma variavel apenas com o texto desse trecho do HTML filtrado acima
text = (filtro_divs[2].get_text())

#Escreve o resultado (text) em um documento. Se não definir o encoder dá erro. Se não existir um arquivo, ele cria.
with open("my_AI_Intel.txt","w", encoding="utf-8") as f:
    f.write(text)
    
#Resumo: Cria um arquivo .txt e salva nele as informações sobre o brasil na Wikipedia.
