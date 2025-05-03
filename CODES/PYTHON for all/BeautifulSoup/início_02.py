import requests
from bs4 import BeautifulSoup

# URL do artigo
url = "https://www.cnnbrasil.com.br/internacional/internado-papa-francisco-inicia-processo-de-reformas-na-igreja-catolica/"

# Enviando requisição para obter o conteúdo da página
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

try:
    # Fazendo a requisição HTTP
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Verifica se houve algum erro na requisição
    
    # Criando o objeto BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Encontrando todas as tags <p>
    paragrafos = soup.find_all('p')
    
    # Imprimindo o texto de cada parágrafo encontrado
    print(f"Foram encontrados {len(paragrafos)} parágrafos:")
    for i, paragrafo in enumerate(paragrafos, 1):
        # Imprimir apenas o texto (sem as tags HTML)
        texto = paragrafo.get_text().strip()
        if texto:  # Verifica se o texto não está vazio
            print(f"\nParágrafo {i}:")
            print(texto)

except requests.exceptions.RequestException as e:
    print(f"Erro ao fazer requisição: {e}")
except Exception as e:
    print(f"Erro inesperado: {e}")