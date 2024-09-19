class TDD_Calculadora:
    def somar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Divisão por zero não é permitida")
        return a / b
    
    def potencia(self, a, b):
        return a ** b