# !pip install langchain
# !pip install langchain-groq

#  GROQ_API_KEY = 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
import os
from langchain_groq import ChatGroq
# API key
api_key='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'
os.environ['GROQ_API_KEY']= api_key
# import modelo
chat= ChatGroq(model='llama-3.3-70b-versatile' )
#  pergunta e resposta usando chat.invoke
resposta= chat.invoke('olá modelo! quem é você e para que é mais recomendado?')
# print(resposta.content)
resposta= chat.invoke('Calcule um investimento de juros compostos inicialmente de 140000 que rende 12% ao ano e pelo prazo de 5 anos, desconte 15% de imposto de renda somente sobre o rendimento, qual o valor total? quanto rendeu nesse perírodo? qual o total de impostos?  ')
print(resposta.content)


