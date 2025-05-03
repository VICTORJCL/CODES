import os
import time
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import YoutubeLoader

api_key = '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'
os.environ['GROQ_API_KEY'] = api_key

chat = ChatGroq(model='llama-3.1-70b-versatile')

# Carregar vídeo do YouTube
url = 'https://www.youtube.com/watch?v=h7JLP89VmMc'
loader = YoutubeLoader.from_youtube_url(
    url,
    language=['pt']
)
lista_documentos = loader.load()

# Dividir o conteúdo em chunks menores (reduzido para 4000 caracteres)
def dividir_texto(texto, tamanho_chunk=4000):
    palavras = texto.split()
    chunks = []
    chunk_atual = []
    contagem_caracteres = 0
    
    for palavra in palavras:
        chunk_atual.append(palavra)
        contagem_caracteres += len(palavra) + 1
        
        if contagem_caracteres >= tamanho_chunk:
            chunks.append(' '.join(chunk_atual))
            chunk_atual = []
            contagem_caracteres = 0
    
    if chunk_atual:
        chunks.append(' '.join(chunk_atual))
    
    return chunks

# Processar o conteúdo
documento_completo = ''
for doc in lista_documentos:
    documento_completo += doc.page_content

chunks = dividir_texto(documento_completo)

# Template para análise
template = ChatPromptTemplate.from_messages([
    ('system', '''Você é um assistente que está analisando uma parte de uma transcrição. 
    Extraia apenas os pontos principais desta parte, seja breve: {informacoes}'''),
    ('user', '{input}')
])

chain_youtube = template | chat

# Processar cada chunk e combinar as respostas
todas_analises = []
for i, chunk in enumerate(chunks):
    print(f"\nProcessando parte {i+1} de {len(chunks)}...")
    
    try:
        resposta = chain_youtube.invoke({
            'informacoes': chunk, 
            'input': 'Liste brevemente os pontos principais desta parte.'
        })
        todas_analises.append(resposta.content)
        
        # Aguardar 10 segundos entre as requisições
        if i < len(chunks) - 1:  # Não espera após o último chunk
            print("Aguardando para processar próxima parte...")
            time.sleep(10)
            
    except Exception as e:
        print(f"Erro ao processar parte {i+1}: {str(e)}")
        continue

# Dividir o resumo final em partes menores
analises_resumidas = "\n".join(todas_analises)
chunks_finais = dividir_texto(analises_resumidas, 3000)

print("\nGerando resumo final...")

# Processar cada chunk do resumo final separadamente
resumos_finais = []
template_final = ChatPromptTemplate.from_messages([
    ('system', '''Você é um assistente que vai criar um resumo baseado em análises de um podcast.
    Seja conciso ao combinar os seguintes pontos em um resumo: {informacoes}'''),
    ('user', '{input}')
])

chain_final = template_final | chat

for i, chunk in enumerate(chunks_finais):
    try:
        time.sleep(10)  # Esperar entre os chunks finais também
        resumo_parcial = chain_final.invoke({
            'informacoes': chunk,
            'input': 'Resuma os pontos principais mencionados.'
        })
        resumos_finais.append(resumo_parcial.content)
    except Exception as e:
        print(f"Erro ao gerar resumo parcial {i+1}: {str(e)}")

print("\nResumo Final do Podcast:")
for i, resumo in enumerate(resumos_finais, 1):
    print(f"\nParte {i}:")
    print(resumo)