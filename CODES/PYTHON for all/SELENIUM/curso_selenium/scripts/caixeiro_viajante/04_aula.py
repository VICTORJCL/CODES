# ADICIONA N DESTINOS
# cria função adiciona_caixa_de_destino

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from time import sleep


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(2)
driver.get("https://www.google.com/maps")


def esta_na_aba_de_rotas():
    xpath = '//button[@aria-label="Fechar rotas"]'
    botao_rotas = driver.find_elements(By.XPATH, xpath)
    return len(botao_rotas) > 0

def adiciona_destino(endereco, num_caixa=1):
    if not esta_na_aba_de_rotas():
        barra_vazia = driver.find_element(By.ID, 'searchboxinput')
        barra_vazia.clear()
        barra_vazia.send_keys(endereco)
        barra_vazia.send_keys(Keys.RETURN)
    else:
        xpath = '//div[contains(@id, "directions-searchbox")]//input'
        caixas = driver.find_elements(By.XPATH, xpath)
        caixas = [c for c in caixas if c.is_displayed()]
        if len(caixas) >= num_caixa:
            caixa_endereco = caixas[num_caixa-1]
            caixa_endereco.send_keys(Keys.CONTROL + 'a')
            caixa_endereco.send_keys(Keys.DELETE)
            caixa_endereco.send_keys(endereco)
            caixa_endereco.send_keys(Keys.RETURN)
        else:
            print(f'Não conseguiimos adicionar o endereço {len(caixas)} | {num_caixa}')

def abre_rotas():
    xpath = '//button[@data-value="Rotas"]'
    wait = WebDriverWait(driver, timeout=5)
    botao_rotas = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    botao_rotas.click()

    xpath = '//button[@aria-label="Fechar rotas"]'
    wait = WebDriverWait(driver, timeout=5)
    botao_rotas = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))

def adiciona_caixa_destino():
    xpath = '//span[text()="Adicionar destino"]'
    wait = WebDriverWait(driver, timeout=3)
    wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

    botao_adiciona_destino = driver.find_element(By.XPATH, xpath)
    botao_adiciona_destino.click()


if __name__ == '__main__':

    enderecos = [
                "Av. José Bonifácio, 245 - Farroupilha, Porto Alegre - RS, 90040-130",  #Redenção
                "Av. Borges de Medeiros, 2035 - Menino Deus, Porto Alegre - RS, 90110-150",  #Marinha
                "Av. Guaíba, 544 - Ipanema, Porto Alegre - RS, 91760-740", #Orla Ipanema
                "Av. Padre Cacique, 2000 - Praia de Belas, Porto Alegre - RS, 90810-180", # Iberê
                ]
    adiciona_destino(enderecos[0], 1)
    abre_rotas()

    adiciona_destino(enderecos[0], 1)
    adiciona_destino(enderecos[1], 2)

    adiciona_caixa_destino()
    adiciona_destino(enderecos[2], 3)

    adiciona_caixa_destino()
    adiciona_destino(enderecos[3], 4)

    sleep(600)

