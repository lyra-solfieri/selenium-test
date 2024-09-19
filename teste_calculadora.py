from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Função para abrir a calculadora
def abrir_calculadora():
    driver = webdriver.Chrome()
    driver.get("https://www.calculadoraonline.com.br/basica")
    time.sleep(1)
    return driver

# Função para clicar nos botões da calculadora
def clicar_botao(driver, valor):
    botao = driver.find_element(By.XPATH, f"//input[@value='{valor}']")
    botao.click()

# Função para pegar o resultado da calculadora
def pegar_resultado(driver):
    return driver.find_element(By.ID, "tela").get_attribute('value')

# Funções para testar as operações
def teste_adicao(driver, valor1, valor2, resultado_esperado):
    clicar_botao(driver, valor1)
    clicar_botao(driver, '+')
    clicar_botao(driver, valor2)
    clicar_botao(driver, '=')
    
    resultado = pegar_resultado(driver)
    assert resultado == str(resultado_esperado), f"Erro: esperado {resultado_esperado}, mas obteve {resultado}"

def teste_subtracao(driver, valor1, valor2, resultado_esperado):
    clicar_botao(driver, valor1)
    clicar_botao(driver, '-')
    clicar_botao(driver, valor2)
    clicar_botao(driver, '=')
    
    resultado = pegar_resultado(driver)
    assert resultado == str(resultado_esperado), f"Erro: esperado {resultado_esperado}, mas obteve {resultado}"

def teste_multiplicacao(driver, valor1, valor2, resultado_esperado):
    clicar_botao(driver, valor1)
    clicar_botao(driver, 'x')
    clicar_botao(driver, valor2)
    clicar_botao(driver, '=')
    
    resultado = pegar_resultado(driver)
    assert resultado == str(resultado_esperado), f"Erro: esperado {resultado_esperado}, mas obteve {resultado}"

def teste_divisao(driver, valor1, valor2, resultado_esperado):
    clicar_botao(driver, valor1)
    clicar_botao(driver, '/')
    clicar_botao(driver, valor2)
    clicar_botao(driver, '=')
    
    resultado = pegar_resultado(driver)
    assert resultado == str(resultado_esperado), f"Erro: esperado {resultado_esperado}, mas obteve {resultado}"

def teste_exponenciacao(driver, valor1, valor2, resultado_esperado):
    clicar_botao(driver, valor1)
    clicar_botao(driver, 'x^n')
    clicar_botao(driver, valor2)
    clicar_botao(driver, '=')
    
    resultado = pegar_resultado(driver)
    assert resultado == str(resultado_esperado), f"Erro: esperado {resultado_esperado}, mas obteve {resultado}"
