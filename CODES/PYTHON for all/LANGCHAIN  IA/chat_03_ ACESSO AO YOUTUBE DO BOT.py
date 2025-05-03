# !pip install langchain==0.3.0
# !pip install langchain-groq==0.2.0
# !pip install langchain-community==0.3.0
# !pip install youtube_transcript_api==0.6.2
# !pip install pypdf==5.0.0

import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate

api_key = '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'
os.environ['GROQ_API_KEY'] = api_key

chat = ChatGroq(model='llama-3.1-70b-versatile')

# acessando vídeos do youtube
from langchain_community.document_loaders import YoutubeLoader
# url  coloquei um podcast do Eslen
url= 'https://www.youtube.com/watch?v=h7JLP89VmMc'

#  carregamento e load do conteúdo
loader = YoutubeLoader.from_youtube_url(
    url,
    language=['pt']
)
lista_documentos = loader.load()

# interação do conteúdo em uma única string em soma string
documento=''
for doc in lista_documentos:
    documento+=doc.page_content

# print(documento)
#  criação do template de informações do bot
template = ChatPromptTemplate.from_messages([
    ('system', 'Você é um assistente amigável que possui as seguintes informações para formular uma resposta: {informacoes}'),
    ('user', '{input}')
])

# chain 
chain_youtube = template | chat
# pergunta do usuário com print da resposta
resposta = chain_youtube.invoke({'informacoes': documento, 'input': 'quais são os pontos principais do podcast do Eslen e quais as maiores "sacadas"?'})
print(resposta.content)

