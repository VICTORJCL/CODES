# !pip install langchain==0.3.0
# !pip install langchain-groq==0.2.0

import os
from langchain_groq import ChatGroq

api_key = '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'
os.environ['GROQ_API_KEY'] = api_key

chat = ChatGroq(model='llama-3.1-70b-versatile')

# importando e criando um template de prompt
from langchain.prompts import ChatPromptTemplate
# template
template = ChatPromptTemplate.from_messages(
    [
        ('system', 'Você é um assistente que sempre responde com piadas'),
        ('user', 'Traduza {expressao} para a lingua {lingua}')
    ]
)
chain = template | chat   # criando a chain, ela relaciona o template com o chat

resposta = chain.invoke({'expressao': 'dei no pé?', 'lingua': 'inglesa'})
print(resposta.content)