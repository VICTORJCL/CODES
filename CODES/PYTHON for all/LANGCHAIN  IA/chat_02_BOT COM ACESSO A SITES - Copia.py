# !pip install langchain==0.3.0
# !pip install langchain-groq==0.2.0
# !pip install langchain-community==0.3.0
# pip install beautifulsoup4

import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate

api_key = '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'
os.environ['GROQ_API_KEY'] = api_key

chat = ChatGroq(model='llama-3.1-70b-versatile')

#  importando e usando um site para obter as informações
from langchain_community.document_loaders import WebBaseLoader
#  site a ser colhida as informações
loader= WebBaseLoader("https://asimov.academy/")
lista_documentos= loader.load()

# pega as informações e soma strings na variável documentos
documento=''
for doc in lista_documentos:
    documento+=doc.page_content
# print(documento)

# funcionamento específico e orientação do bot
template= ChatPromptTemplate.from_messages([
    ('system', 'Você é um assistente amigável chamado Asimo e tem acesso as seguinte informações para dar as suas respostas: {documentos_informados}'),
    ('user','{input}')
])

chain=template | chat
resposta = chain.invoke({'documentos_informados': documento, 'input': 'elabore um teste de 10 mil linhas sobre a asimov'})

#  print da resposta do assistente
print(resposta.content) 