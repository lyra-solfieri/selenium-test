import unittest
from tdd_calculadora import TDD_Calculadora

class TestCalculadora(unittest.TestCase):
    
    def setUp(self):
        self.calc = TDD_Calculadora()

    # Teste TDD para soma
    def test_soma(self):
        resultado = self.calc.somar(2, 3)
        self.assertEqual(resultado, 5)

    # Teste TDD para subtração
    def test_subtracao(self):
        resultado = self.calc.subtrair(10, 4)
        self.assertEqual(resultado, 6)

    # Teste TDD para multiplicação(irá falhar)
    def test_multiplicacao(self):
        resultado = self.calc.multiplicar(3, 3)
        self.assertEqual(resultado, 9)

    # Teste TDD para divisão
    def test_divisao(self):
        resultado = self.calc.dividir(8, 2)
        self.assertEqual(resultado, 4)
        
    # TDD para potencia
    def test_potencia(self):
        resultado = self.calc.potencia(2,2)
        self.assertEqual(resultado,4)

    # Teste para divisão por zero
    def test_divisao_por_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.dividir(5, 0)
    

if __name__ == '__main__':
    unittest.main()
