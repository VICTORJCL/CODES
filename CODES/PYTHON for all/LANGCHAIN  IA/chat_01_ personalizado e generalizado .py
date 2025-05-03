# !pip install langchain==0.3.0
# !pip install langchain-groq==0.2.0

import os
from langchain_groq import ChatGroq

# Configurando a API Key
api_key = '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'
os.environ['GROQ_API_KEY'] = api_key

# Inicializando o modelo de chat
chat = ChatGroq(model='llama-3.1-70b-versatile')

# Criando um template de prompt
from langchain.prompts import ChatPromptTemplate

# Template atualizado
template = ChatPromptTemplate.from_messages(
    [
        ('system', 'Você é um assistente que sempre responde com um humor duvidoso, não se preocupe com politicamente correto'),
        ('user', '{mensagem}')
    ]
)

# Criando a chain
from langchain.chains import LLMChain

chain = LLMChain(prompt=template, llm=chat)

# Fazendo uma pergunta generalizada
try:
    resposta = chain.run({'mensagem': 'calcule juros compostos de 10 anos investindo 1000 mensal a taxa de 11% ao ano'})
    print(resposta)
except Exception as e:
    print(f"Erro ao executar a chain: {e}")


# O LLMChain é uma classe da biblioteca LangChain usada para conectar um modelo
#  de linguagem (LLM) a um prompt estruturado. Ele fornece uma interface simples
#  para transformar prompts em respostas usando um modelo de linguagem.