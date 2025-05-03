from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
try:
    driver.get("https://www.youtube.com")
    sleep(4)

    botao = driver.find_elements(By.CLASS_NAME, 'title style-scope ytd-guide-entry-renderer')
    botao.click()

    #     # Opção 1: Usando XPath
    # botao = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, "//a[@aria-label='Twitter']"))
    # )
    # botao.click()
    
    # Opção 2: Usando seletor CSS
    # botao = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.CSS_SELECTOR, "a[aria-label='Twitter']"))
    # )
    # botao.click()
    


except Exception as e:
 
    print(f"Ocorreu um erro: {e}")

'''
text_box = driver.find_element(by=By.CLASS_NAME, value='text-body font-medium text-gray-800 guru-sm:text-body2')

submit_button = driver.find_element(by=By.CSS_SELECTOR, value='button')
submit_button.click()

message = driver.find_element(by=By.ID, value="message")
print('Mensagem final', message.text)

sleep(30)
'''