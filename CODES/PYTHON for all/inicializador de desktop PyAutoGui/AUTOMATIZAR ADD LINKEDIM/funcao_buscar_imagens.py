import pyautogui
from time import sleep
import os
# Obtém o diretório do arquivo atual
caminho_atual = os.path.dirname(os.path.abspath(__file__))
# Define o diretório de trabalho como o diretório do arquivo
os.chdir(caminho_atual)

import os
# Obtém o diretório do arquivo atual
caminho_atual = os.path.dirname(os.path.abspath(__file__))
# Define o diretório de trabalho como o diretório do arquivo
os.chdir(caminho_atual)


def clica_na_imagem(img):
    """
    Função para localizar e clicar em uma imagem na tela.
    Retorna True se encontrou e clicou, False caso contrário.
    """
    try:
        # Corrigindo o caminho para apontar para a pasta correta
        imagem = f"{caminho_atual}/img/{img}.png"
        # imagem = f"C:/PYTHON for All/inicializador de desktop PyAutoGui/AUTOMATIZAR ADD LINKEDIM/img/{img}.png"
        imagem = f"{caminho_atual}/img/{img}.png"
        # imagem = f"C:/PYTHON for All/inicializador de desktop PyAutoGui/AUTOMATIZAR ADD LINKEDIM/img/{img}.png"
        
        # Tentativa de localizar a imagem
        local_imagem = pyautogui.locateOnScreen(imagem, confidence=0.9)
        
        if local_imagem is not None:
            pyautogui.click(local_imagem)
            return True
        else:
            print(f"Imagem {img} não encontrada na tela")
            return False
    except Exception as e:
        pass
