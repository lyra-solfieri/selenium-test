from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import xml.etree.ElementTree as ET

class Calculadora:
    
    ARQUIVO_XML  = 'dados_testes.xml'
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.calculadoraonline.com.br/basica")
        time.sleep(2)

    def finalizar_driver(self):
        self.driver.quit()
        
    def _carregar_dados_xml(self):
        tree = ET.parse(self.ARQUIVO_XML)
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
 
    def executar_procedimento(self, nome_procedimento, casos):
        driver = self.driver
        
        operacoes = {
            'multiplicacao': '*',
            'divisao': '/',
            'subtracao': '-',
            'soma': '+',
            'potenciacao': '^'
        }
        
        nome_procedimento_formatado = nome_procedimento.replace(' ', '').lower()
        simbolo_operacao = operacoes.get(nome_procedimento_formatado, '')

        resultados = []
        for entrada1, entrada2, resultado_esperado in casos:
            
            # Limpar o campo de entrada da calculadora
            input_field = driver.find_element(By.ID, 'TIExp')
            input_field.clear()

            
            # Inserir a expressão matemática no campo de entrada
            expressao = f"{entrada1}{simbolo_operacao}{entrada2}"
            input_field.send_keys(expressao)


            # Aguardar 1 segundo para a execução do cálculo
            time.sleep(1)

            # Obter o resultado atual exibido pela calculadora
            resultado_atual = driver.find_element(By.ID, 'LBSubResu').text
            
            # Armazenar o resultado atual e o esperado para validação posterior
            resultados.append((resultado_atual, resultado_esperado))
        
        return resultados
