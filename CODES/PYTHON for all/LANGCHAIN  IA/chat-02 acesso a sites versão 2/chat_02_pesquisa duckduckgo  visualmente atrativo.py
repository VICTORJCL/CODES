import tkinter as tk
from tkinter import ttk, scrolledtext
import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.tools import DuckDuckGoSearchResults
from threading import Thread
import json
from datetime import datetime
import customtkinter as ctk

class ChatbotGUI:
    def __init__(self):
        # Configurar janela principal
        self.window = ctk.CTk()
        self.window.title("🤖 Asimo Web Explorer")
        self.window.geometry("1000x800")
        ctk.set_appearance_mode("dark")
        
        # Configurar API keys
        os.environ["USER_AGENT"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        os.environ['GROQ_API_KEY'] = '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'
        
        # Inicializar chat
        self.chat = ChatGroq(model='llama-3.1-70b-versatile')
        
        # Criar template do chat
        self.template = ChatPromptTemplate.from_messages([
            ('system', '''Você é um assistente amigável chamado Asimo que analisa informações da web.
            Use as seguintes informações para responder: {documentos_informados}
            
            Importante: Sempre cite as fontes das informações ao final da resposta.'''),
            ('user', '{input}')
        ])
        
        self.chain = self.template | self.chat
        
        # Configurar interface
        self.setup_gui()
        
    def setup_gui(self):
        # Frame principal
        main_frame = ctk.CTkFrame(self.window)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Título
        title_label = ctk.CTkLabel(
            main_frame,
            text="Asimo Web Explorer",
            font=("Helvetica", 24, "bold")
        )
        title_label.pack(pady=10)
        
        # Área de chat
        self.chat_area = ctk.CTkTextbox(
            main_frame,
            font=("Helvetica", 14),
            height=500,
            wrap=tk.WORD
        )
        self.chat_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Frame de entrada
        input_frame = ctk.CTkFrame(main_frame)
        input_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Campo de entrada
        self.input_field = ctk.CTkEntry(
            input_frame,
            placeholder_text="Digite sua pergunta aqui...",
            font=("Helvetica", 14),
            height=40
        )
        self.input_field.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        
        # Botão de envio
        self.send_button = ctk.CTkButton(
            input_frame,
            text="Enviar",
            font=("Helvetica", 14),
            command=self.process_input,
            height=40
        )
        self.send_button.pack(side=tk.RIGHT)
        
        # Bind Enter key
        self.input_field.bind("<Return>", lambda e: self.process_input())
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Pronto para pesquisar!")
        self.status_label = ctk.CTkLabel(
            main_frame,
            textvariable=self.status_var,
            font=("Helvetica", 12)
        )
        self.status_label.pack(pady=5)
        
    def pesquisar_e_coletar(self, query):
        self.status_var.set("Pesquisando...")
        self.window.update()
        
        search = DuckDuckGoSearchResults()
        informacoes = []
        fontes = []
        
        try:
            results = search.run(query)
            
            for result in eval(results):
                try:
                    url = result['link']
                    loader = WebBaseLoader(url)
                    docs = loader.load()
                    informacoes.append(docs[0].page_content)
                    fontes.append(f"{result['title']} - {url}")
                except Exception as e:
                    continue
                    
        except Exception as e:
            self.status_var.set(f"Erro na pesquisa: {str(e)}")
            
        return informacoes, fontes
    
    def add_message(self, message, is_user=False):
        timestamp = datetime.now().strftime("%H:%M")
        self.chat_area.configure(state=tk.NORMAL)
        
        # Adicionar quebra de linha se necessário
        if self.chat_area.get("1.0", tk.END).strip():
            self.chat_area.insert(tk.END, "\n\n")
        
        # Formatar mensagem
        prefix = f"Você [{timestamp}]:" if is_user else f"Asimo [{timestamp}]:"
        self.chat_area.insert(tk.END, f"{prefix}\n", "bold")
        self.chat_area.insert(tk.END, message)
        
        self.chat_area.configure(state=tk.DISABLED)
        self.chat_area.see(tk.END)
        
    def process_input(self):
        query = self.input_field.get()
        if not query.strip():
            return
            
        # Limpar campo de entrada
        self.input_field.delete(0, tk.END)
        
        # Adicionar mensagem do usuário
        self.add_message(query, is_user=True)
        
        # Desabilitar entrada durante processamento
        self.input_field.configure(state=tk.DISABLED)
        self.send_button.configure(state=tk.DISABLED)
        
        # Iniciar thread de processamento
        Thread(target=self.process_query, args=(query,)).start()
        
    def process_query(self, query):
        try:
            # Pesquisar e coletar informações
            informacoes, fontes = self.pesquisar_e_coletar(query)
            
            if not informacoes:
                self.add_message("Desculpe, não consegui encontrar informações sobre isso.")
                return
            
            # Preparar documento
            documento_completo = "\n\n".join(informacoes)
            documento_completo += "\n\nFontes consultadas:\n" + "\n".join(fontes)
            
            # Gerar resposta
            self.status_var.set("Analisando informações...")
            self.window.update()
            
            resposta = self.chain.invoke({
                'documentos_informados': documento_completo,
                'input': query
            })
            
            # Adicionar resposta
            self.add_message(resposta.content)
            
        except Exception as e:
            self.add_message(f"Ocorreu um erro: {str(e)}")
            
        finally:
            # Reabilitar entrada
            self.input_field.configure(state=tk.NORMAL)
            self.send_button.configure(state=tk.NORMAL)
            self.status_var.set("Pronto para pesquisar!")
            self.window.update()
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    # Instalar dependências necessárias
    os.system("pip install customtkinter")
    os.system("pip install duckduckgo-search")
    
    # Iniciar aplicação
    app = ChatbotGUI()
    app.run()