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


#  acessando PDFS
from langchain_community.document_loaders import PyPDFLoader
caminho="E:\\USUÁRIO\DOWLOADS\\029 - COMO SE COMPORTAR EM UMA ENTREVISTA DE EMPREGO (usando as neurociências).pdf"
loader= PyPDFLoader(caminho)
lista_documentos= loader.load()

# armazenando e interando strings do conteúdo:
documento = ''
for doc in lista_documentos:
  documento = documento + doc.page_content

#  template e informações do bot
template = ChatPromptTemplate.from_messages([
    ('system', 'Você é um assistente amigável que possui as seguintes informações para formular uma resposta: {informacoes}'),
    ('user', '{input}')
])

#  chain e pergunta do usuário
chain_youtube = template | chat
resposta = chain_youtube.invoke({'informacoes': documento, 'input': 'Afinal, segundo o documento, qual é a melhor forma de se portar em uma entrevista de emprego? dê exemplos e principais "sacadas"'})
print(resposta.content)