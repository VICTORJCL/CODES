import os
import pyautogui
import os
from time import sleep
from dotenv import load_dotenv
import webbrowser
import time # tempo
from datetime import datetime, timedelta # tempo

# Obtém o diretório do arquivo atual
caminho_atual = os.path.dirname(os.path.abspath(__file__))
# Define o diretório de trabalho como o diretório do arquivo
os.chdir(caminho_atual)

from funcao_buscar_imagens import clica_na_imagem

load_dotenv()

# curitiba e região, tech recruiter
webbrowser.open('https://www.linkedin.com/search/results/people/?geoUrn=%5B%2290009579%22%5D&keywords=%22tech%20recruiter%22%20and%20%22Talent%20Acquisition%22&origin=GLOBAL_SEARCH_HEADER&sid=C3F')
# pyautogui.write("tech recruiter", interval=0.10)
sleep(3)
def conectar():
    for i in range(5):
        clica_na_imagem('conectar')
        sleep(0.5)
        clica_na_imagem('enviar')
        sleep(0.2)
def seguir():
    for i in range(5):
        clica_na_imagem('seguir')
seguir()
conectar()
sleep(1)
pyautogui.press("pagedown")

def add_linkedim():
    # Define o tempo de término (10 minutos a partir de agora)
    tempo_final = datetime.now() + timedelta(minutes=10)
    
    try:
        while datetime.now() < tempo_final:
            # Seu código aqui
            seguir()
            conectar()
            pyautogui.press("pagedown")
            sleep(0.3)
            seguir()
            conectar()
            clica_na_imagem('avancar')
            
            
            # pequeno delay para não sobrecarregar o CPU
            time.sleep(1.5)  
            print(tempo_final) 
    except KeyboardInterrupt:
        pass


add_linkedim()





# webbrowser.open('https://www.linkedin.com/in/victor-jos%C3%A9-costta-lameiro-09b3a8258/')
''' beta_1
sleep(3)
clica_na_imagem('Pesquisa')
pyautogui.write("tech recruiter", interval=0.10)
pyautogui.press("enter")
sleep(3)
clica_na_imagem('pessoas')
sleep(2)

pyautogui.press("pagedown")
sleep(1)
clica_na_imagem('conectar')
sleep(1)
clica_na_imagem('enviar')
'''


'''
sleep(1)
pyautogui.hotkey("ctrl", "shift", "n")
sleep(1)
pyautogui.hotkey("ctrl", "l")
sleep(1)
pyautogui.write("RSCL3 ", interval=0.10)
pyautogui.press("enter")
sleep(1)
pyautogui.press("pagedown")
pyautogui.press("pagedown")


clica_na_imagem('Icon_Tradingview')
sleep(1)
pyautogui.press("enter")

 lista de coisas pyautogui
pyautogui.hotkey("ctrl", "shift", "n")
pyautogui.write("google", interval=0.10)
pyautogui.press("space")
pyautogui.write("globo.com", interval=0.10)
pyautogui.write(SENHA_GOOGLE, interval=0.10)
sleep(1)
'''