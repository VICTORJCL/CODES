from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from time import sleep


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://jovemnerd.com.br/')
sleep(5)
xpath_im='//img[@src="https://uploads.jovemnerd.com.br/wp-content/uploads/2025/02/mau_acompanhado_138_site__asg5013-scaled.jpg?ims=408x230/filters:quality(75)"]'
pesquisa1=driver.find_element(By.XPATH, xpath_im)
pesquisa1.click
driver.fullscreen_window()
try:

    pass
except Exception as e:
 
    print(f"Ocorreu um erro: {e}")
