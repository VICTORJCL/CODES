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


def resposta_bot(mensagens):
  mensagens_modelo = [('system', 'Você é um assistente amigável chamado Asimo')]
  mensagens_modelo += mensagens
  template = ChatPromptTemplate.from_messages(mensagens_modelo)
  chain = template | chat
  return chain.invoke({}).content

#  carregamento esqueleto
def carrega_site():
  url_site = input('Digite a url do site: ')
  documento = ''
  return documento

def carrega_pdf():
  documento = 'Digite o caminho do arquivo pdf'
  return documento

def carrega_youtube():
  url_youtube = input('Digite a url do vídeo: ')
  documento = ''
  return documento

print('Bem-vindo ao AsimoBot')

texto_selecao = '''Digite 1 se você quiser conversar com um site
Digite 2 se você quiser conversar com um pdf
Digite 3 se você quiser conversar com um vídeo de youtube '''

while True:
  selecao = input(texto_selecao)
  if selecao == '1':
    documento = carrega_site()
    break
  if selecao == '2':
    documento = carrega_pdf()
    break
  if selecao == '3':
    documento = carrega_youtube()
    break
  print('Digite um valor entre 1 e 3')


mensagens = []
while True:
  pergunta = input('Usuario: ')
  if pergunta.lower() == 'x':
    break
  mensagens.append(('user', pergunta))
  resposta = resposta_bot(mensagens)
  mensagens.append(('assistant', resposta))
  print(f'Bot: {resposta}')

print('Muito obrigado por usar o AsimoBot')