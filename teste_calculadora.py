from selenium import webdriver
from selenium.webdriver.common.by import By

# Caminho para o WebDriver (substitua pelo caminho correto do seu WebDriver)
driver_path = "caminho/para/chromedriver"

# Criar uma instância do WebDriver
driver = webdriver.Chrome(executable_path=driver_path)

# Acessar uma página da web
driver.get("https://www.google.com")

# Encontrar um elemento (exemplo: campo de pesquisa) e interagir com ele
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium Python")
search_box.submit()

# Fechar o navegador após a automação
driver.quit()
