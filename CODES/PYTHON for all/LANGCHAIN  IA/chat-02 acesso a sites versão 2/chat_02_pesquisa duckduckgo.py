# Para que o chat possa "viajar" pela internet e coletar informações de múltiplos sites automaticamente, 
# podemos usar uma combinação de WebBaseLoader com um motor de busca. Vou criar um exemplo usando o 
# DuckDuckGo para pesquisar e coletar informações:
import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.tools import DuckDuckGoSearchResults

# Configurações iniciais
os.environ["USER_AGENT"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
api_key = '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'
os.environ['GROQ_API_KEY'] = api_key
chat = ChatGroq(model='llama-3.1-70b-versatile')

def pesquisar_e_coletar(query, num_results=3):
    # Realiza a pesquisa
    search = DuckDuckGoSearchResults()
    results = search.run(query)
    
    # Lista para armazenar as informações e fontes
    informacoes = []
    fontes = []
    
    # Tenta coletar informações de cada resultado
    for result in eval(results):
        try:
            url = result['link']
            loader = WebBaseLoader(url)
            docs = loader.load()
            
            # Armazena o conteúdo e a fonte
            informacoes.append(docs[0].page_content)
            fontes.append(url)
            
        except Exception as e:
            continue
    
    return informacoes, fontes

def chat_bot():
    template = ChatPromptTemplate.from_messages([
        ('system', '''Você é um assistente amigável chamado Asimo que analisa informações da web.
        Use as seguintes informações para responder: {documentos_informados}
        
        Importante: Sempre cite as fontes das informações ao final da resposta.'''),
        ('user', '{input}')
    ])
    
    chain = template | chat
    
    while True:
        pergunta = input("\nO que você gostaria de saber? (ou 'sair' para encerrar): ")
        
        if pergunta.lower() == 'sair':
            print("\nAté logo!")
            break
            
        print("\nPesquisando na web...")
        informacoes, fontes = pesquisar_e_coletar(pergunta)
        
        if not informacoes:
            print("Desculpe, não consegui encontrar informações sobre isso.")
            continue
            
        # Junta todas as informações coletadas
        documento_completo = "\n\n".join(informacoes)
        documento_completo += "\n\nFontes consultadas:\n" + "\n".join(fontes)
        
        print("\nProcessando informações encontradas...")
        
        resposta = chain.invoke({
            'documentos_informados': documento_completo,
            'input': pergunta
        })
        
        print("\nResposta do Asimo:")
        print(resposta.content)

# Iniciando o chat
if __name__ == "__main__":
    # Primeiro, vamos instalar as dependências necessárias
    print("Instalando dependências necessárias...")
    os.system("pip install duckduckgo-search")
    
    print("\nBem-vindo ao Asimo! Posso pesquisar e analisar informações da web para você.")
    print("Faça sua pergunta e eu buscarei as informações mais relevantes.")
    chat_bot()