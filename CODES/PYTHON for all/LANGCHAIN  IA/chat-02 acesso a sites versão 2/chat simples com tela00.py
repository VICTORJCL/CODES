import tkinter as tk
from tkinter import scrolledtext
import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
import customtkinter as ctk

# Configurar API Key para o ChatGroq
api_key = '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'
os.environ['GROQ_API_KEY'] = api_key

# Inicializar o modelo de chat
chat = ChatGroq(model='llama-3.1-70b-versatile')

def resposta_bot(
        
        
):
    """Função para gerar resposta do bot baseado nas mensagens."""
    mensagens_modelo = [('system', 'Você é um assistente amigável chamado Asimo')]
    mensagens_modelo += mensagens
    template = ChatPromptTemplate.from_messages(mensagens_modelo)
    chain = template | chat
    return chain.invoke({}).content

class AsimoBotGUI:
    def __init__(self):
        # Configurar janela principal
        self.window = ctk.CTk()
        self.window.title("🤖 AsimoBot")
        self.window.geometry("800x600")
        ctk.set_appearance_mode("dark")
        
        # Inicializar lista de mensagens
        self.mensagens = []
        
        # Criar interface gráfica
        self.setup_gui()
    
    def setup_gui(self):
        """Configura a interface gráfica."""
        # Frame principal
        main_frame = ctk.CTkFrame(self.window)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Título
        title_label = ctk.CTkLabel(main_frame, text="AsimoBot", font=("Helvetica", 24, "bold"))
        title_label.pack(pady=10)
        
        # **Saída do Chat**: Área de texto para exibir mensagens
        self.chat_area = scrolledtext.ScrolledText(
        main_frame, font=("Helvetica", 14), wrap=tk.WORD, state=tk.DISABLED, height=20, bg="black", fg="white"
        )
        self.chat_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Frame de entrada de texto
        input_frame = ctk.CTkFrame(main_frame)
        input_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # **Entrada do Usuário**: Campo para digitar mensagens
        self.input_field = ctk.CTkEntry(input_frame, placeholder_text="Digite sua pergunta...", font=("Helvetica", 14), height=40)
        self.input_field.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        
        # Botão para enviar mensagem
        self.send_button = ctk.CTkButton(input_frame, text="Enviar", font=("Helvetica", 14), command=self.enviar_mensagem, height=40)
        self.send_button.pack(side=tk.RIGHT)
        
        # Bind para tecla Enter
        self.input_field.bind("<Return>", lambda e: self.enviar_mensagem())
    
    def adicionar_mensagem(self, mensagem, is_user=False):
        """Adiciona mensagens no histórico do chat."""
        self.chat_area.configure(state=tk.NORMAL)
        prefixo = "Você: " if is_user else "Asimo: "
        self.chat_area.insert(tk.END, f"{prefixo}{mensagem}\n")
        self.chat_area.configure(state=tk.DISABLED)
        self.chat_area.see(tk.END)
    
    def enviar_mensagem(self):
        """Processa a mensagem do usuário e exibe a resposta."""
        pergunta = self.input_field.get().strip() 
        if not pergunta:
            return
        
        # Adicionar pergunta do usuário ao chat
        self.adicionar_mensagem(pergunta, is_user=True)
        self.input_field.delete(0, tk.END)
        
        # Processar e gerar resposta
        self.mensagens.append(('user', pergunta))
        resposta = resposta_bot(self.mensagens)
        self.mensagens.append(('assistant', resposta))
        self.adicionar_mensagem(resposta, is_user=False)
    
    def run(self):
        """Inicia o loop principal da interface."""
        self.window.mainloop()

# Executar o chatbot
if __name__ == "__main__":
    app = AsimoBotGUI()
    app.run()
