import requests
from bs4 import BeautifulSoup

# URL do artigo
url = "https://www.cnnbrasil.com.br/internacional/internado-papa-francisco-inicia-processo-de-reformas-na-igreja-catolica/"


''' if texto:  # Verifica se o texto não está vazio
paragrafo.get_text().strip()   strip() remove espaços em branco
'''

# Fazendo a requisição HTTP
page = requests.get(url)


# Criando o objeto BeautifulSoup
soup = BeautifulSoup(page.text, 'html.parser')

# resposta=page.text # pega todo conteúdo
# Encontrando todas as tags <p>
tags_p= soup.find_all('p')  
# tags_p= soup.find_all('p', {"class=": 'post_title'})  

#  para pegar todos os p
# for p in tags_p:
#     p.get_text()
    # print(p)

mod=''.join(str(x.get_text())+' \n' for x in tags_p)    # transforma a lista em string, concatena e adiciona quebra de linha
print(mod)






'''
replaces=['<p>','</p>','<div>','</div>','</p><p','<div','<a','<p', '>','<span','</span','</button','class=']
for x in replaces:
    if x == '</p>':
        mod=mod.replace(x,'\n')
    mod=mod.replace(x,'')
'''





