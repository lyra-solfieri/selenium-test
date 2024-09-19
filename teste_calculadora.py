import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # Iniciar o WebDriver e a Calculadora
        cls.calc = Calculadora()

    @classmethod
    def tearDownClass(cls):
        # Finalizar o WebDriver
        cls.calc.finalizar_driver()
            
    def test_calculadora(self):
        procedimentos = self.calc._carregar_dados_xml()
        
        for nome_procedimento, casos in procedimentos.items():
            resultados = self.calc.executar_procedimento(nome_procedimento, casos)
            
            for resultado_atual, resultado_esperado in resultados:
                if resultado_esperado is None:
                    self.assertIn('', resultado_atual)
                else:
                    self.assertEqual(resultado_atual, resultado_esperado)

if __name__ == "__main__":
    unittest.main()
