import unittest
from app import app

class TestCalculadora(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_soma(self):
        response = self.app.post('/', data=dict(num1=2, num2=3, operacao='soma'))
        self.assertIn('Resultado: 5.0', response.data.decode('utf-8'))

    def test_subtracao(self):
        response = self.app.post('/', data=dict(num1=5, num2=3, operacao='subtracao'))
        self.assertIn('Resultado: 2.0', response.data.decode('utf-8'))

    def test_multiplicacao(self):
        response = self.app.post('/', data=dict(num1=2, num2=3, operacao='multiplicacao'))
        self.assertIn('Resultado: 6.0', response.data.decode('utf-8'))

    def test_divisao(self):
        response = self.app.post('/', data=dict(num1=6, num2=3, operacao='divisao'))
        self.assertIn('Resultado: 2.0', response.data.decode('utf-8'))

    def test_divisao_por_zero(self):
        response = self.app.post('/', data=dict(num1=6, num2=0, operacao='divisao'))
        # Aqui estamos verificando a mensagem de erro correta
        self.assertIn('Erro: Divisão por zero', response.data.decode('utf-8'))

    def test_valor_invalido(self):
        response = self.app.post('/', data=dict(num1='a', num2=3, operacao='soma'))
        # Aqui verificamos o erro de valores inválidos
        self.assertIn('Erro: Insira números válidos', response.data.decode('utf-8'))

if __name__ == '__main__':
    unittest.main()
