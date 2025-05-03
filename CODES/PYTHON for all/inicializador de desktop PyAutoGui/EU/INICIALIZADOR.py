import os
import pyautogui
import os
from time import sleep
from dotenv import load_dotenv
'''' lista de coisas pyautogui
pyautogui.hotkey("ctrl", "shift", "n")
pyautogui.write("google", interval=0.10)
pyautogui.press("space")
pyautogui.write("globo.com", interval=0.10)
pyautogui.write(SENHA_GOOGLE, interval=0.10)
sleep(1)
'''
#  kasdkjasd

from funcao_buscar_imagens import clica_na_imagem

# Muda para o diretório da imagem
os.chdir('C:/PYTHON for All/inicializador de desktop/EU/img')

load_dotenv()

# Abrir o Chrome e deixar na página de busca do Google





clica_na_imagem('icone_chrome')  # Sem .png
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