import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.utilities import GoogleSearchAPIWrapper

# Configuração da página
st.set_page_config(
    page_title="Asimo Web Explorer",
    page_icon="🤖",
    layout="wide"
)

# Estilo CSS personalizado
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stTextInput {
        font-size: 1.2rem;
    }
    .chat-message {
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        font-size: 1.1rem;
        line-height: 1.5;
    }
    .sources {
        font-size: 0.9rem;
        color: #666;
        padding: 1rem;
        background-color: #f0f2f6;
        border-radius: 0.5rem;
        margin-top: 1rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Configurações das APIs
if 'initialized' not in st.session_state:
    os.environ["USER_AGENT"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    os.environ["GOOGLE_CSE_ID"] = "seu_search_engine_id"  # Substitua pelo seu ID
    os.environ["GOOGLE_API_KEY"] = "sua_api_key"  # Substitua pela sua API key
    os.environ['GROQ_API_KEY'] = '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'
    st.session_state.chat = ChatGroq(model='llama-3.1-70b-versatile')
    st.session_state.initialized = True

def pesquisar_e_coletar(query, num_results=3):
    search = GoogleSearchAPIWrapper()
    informacoes = []
    fontes = []
    
    try:
        results = search.results(query, num_results)
        
        for result in results:
            try:
                url = result["link"]
                loader = WebBaseLoader(url)
                docs = loader.load()
                informacoes.append(docs[0].page_content)
                fontes.append(f"{result['title']} - {url}")
            except Exception as e:
                continue
                
    except Exception as e:
        st.error(f"Erro na pesquisa: {str(e)}")
        
    return informacoes, fontes

# Título principal
st.title("🤖 Asimo Web Explorer")
st.markdown("### Seu assistente para explorar a web")

# Área de entrada
query = st.text_input("O que você gostaria de saber?", key="user_input", 
                     placeholder="Digite sua pergunta aqui...")

# Botão de pesquisa
if st.button("Pesquisar", type="primary"):
    with st.spinner("Pesquisando na web..."):
        informacoes, fontes = pesquisar_e_coletar(query)
        
        if not informacoes:
            st.error("Desculpe, não consegui encontrar informações sobre isso.")
        else:
            # Preparar e enviar query para o chat
            template = ChatPromptTemplate.from_messages([
                ('system', '''Você é um assistente amigável chamado Asimo que analisa informações da web.
                Analise as seguintes informações para responder: {documentos_informados}
                
                Importante: Forneça respostas bem estruturadas e detalhadas.'''),
                ('user', '{input}')
            ])
            
            chain = template | st.session_state.chat
            
            documento_completo = "\n\n".join(informacoes)
            
            # Processar resposta
            with st.spinner("Analisando informações..."):
                resposta = chain.invoke({
                    'documentos_informados': documento_completo,
                    'input': query
                })
            
            # Exibir resposta
            st.markdown("### Resposta:")
            st.markdown(f'<div class="chat-message">{resposta.content}</div>', 
                       unsafe_allow_html=True)
            
            # Exibir fontes
            st.markdown("### Fontes consultadas:")
            for fonte in fontes:
                st.markdown(f'<div class="sources">{fonte}</div>', 
                          unsafe_allow_html=True)

# Rodapé
st.markdown("---")
st.markdown("Desenvolvido com ❤️ usando Streamlit e LangChain")