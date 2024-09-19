from selenium import webdriver
from selenium.webdriver.common.by import By
<<<<<<< Updated upstream
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
=======
import xml.etree.ElementTree as ET
import unittest
import time

class TestCalculadora(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.calculadoraonline.com.br/basica")

    def tearDown(self):
        self.driver.quit()

    def _carregar_dados_xml(self, arquivo_xml):
        tree = ET.parse(arquivo_xml)
        root = tree.getroot()
        procedimentos = {}
        for procedimento in root.findall('procedimento'):
            nome = procedimento.get('nome')
            casos = []
            for caso in procedimento.findall('caso'):
                entrada1 = caso.find('entrada1').text
                entrada2 = caso.find('entrada2').text
                resultado_esperado = caso.find('resultado_esperado').text
                casos.append((entrada1, entrada2, resultado_esperado))
            procedimentos[nome] = casos
        return procedimentos

    def _executar_procedimento(self, nome_procedimento, casos):
        driver = self.driver
        for entrada1, entrada2, resultado_esperado in casos:

            # Limpar campo de entrada
            input_field = driver.find_element(By.ID, 'TIExp')
            input_field.clear()
            simbolo_operacao = nome_procedimento.replace(' ', '').lower().replace('multiplicacao', '*').replace('divisao', '/').replace('subtracao', '-').replace('soma', '+').replace('potenciacao', '^')
            input_field.send_keys(f"{entrada1}{simbolo_operacao}{entrada2}")  # Formato como "1+2" para soma

            time.sleep(1)

            resultado_atual = driver.find_element(By.ID, 'LBSubResu').text
            
            if resultado_esperado == None:
                self.assertIn('', resultado_atual)
            else:
                self.assertEqual(resultado_atual, resultado_esperado)

    def test_calculadora(self):
        procedimentos = self._carregar_dados_xml('dados_testes.xml')
        for nome_procedimento, casos in procedimentos.items():
            self._executar_procedimento(nome_procedimento, casos)

if __name__ == "__main__":
    unittest.main()
>>>>>>> Stashed changes
