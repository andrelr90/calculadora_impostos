import unittest
from calculadora_imposto_renda import CalculadoraImpostoDeRenda

class TestCalculadoraImpostoDeRenda(unittest.TestCase):
    def setUp(self):
        pass

    def test_salario_menor_que_zero_deve_disparar_excecao(self):
        self.assertRaises(Exception, CalculadoraImpostoDeRenda, -1, True)

    def test_salario_igual_a_zero_nao_deve_disparar_excecao(self):
        try:
            calculadora = CalculadoraImpostoDeRenda(0, True)
        except:
            self.fail()

if __name__ == '__main__':
    unittest.main()