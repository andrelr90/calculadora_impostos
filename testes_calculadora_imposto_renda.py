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

    def test_get_porcentagem_imposto_isento(self):
        calculadora = CalculadoraImpostoDeRenda(0, True)
        self.assertEqual(0, calculadora._get_porcentagem_imposto(1900))

    def test_get_porcentagem_imposto_no_limite_isento(self):
        calculadora = CalculadoraImpostoDeRenda(0, True)
        self.assertEqual(0, calculadora._get_porcentagem_imposto(22847.76))

    def test_get_porcentagem_imposto_no_limiar_inicial_da_proxima_faixa(self):
        calculadora = CalculadoraImpostoDeRenda(0, True)
        self.assertEqual(0.075, calculadora._get_porcentagem_imposto(22847.77))

    def test_get_porcentagem_imposto_na_ultima_faixa(self):
        calculadora = CalculadoraImpostoDeRenda(0, True)
        self.assertEqual(0.275, calculadora._get_porcentagem_imposto(100000.77))

    def test_get_valor_salario_anual_com_13_deve_ser_13_vezes_o_mensal(self):
        calculadora = CalculadoraImpostoDeRenda(1900, True)
        self.assertEqual(24700, calculadora._get_salario_anual())

    def test_get_valor_salario_anual_sem_13_deve_ser_12_vezes_o_mensal(self):
        calculadora = CalculadoraImpostoDeRenda(1900, False)
        self.assertEqual(22800, calculadora._get_salario_anual())
        
    def test_get_valor_imposto_anual_isento_deve_ser_0(self):
        calculadora = CalculadoraImpostoDeRenda(1000, True)
        self.assertEqual(0, calculadora.get_valor_imposto_anual())

    def test_get_valor_imposto_anual_com_salario_na_ultima_faixa_deve_ser_27_5_por_cento(self):
        calculadora = CalculadoraImpostoDeRenda(35000, True)
        self.assertAlmostEqual(125125, calculadora.get_valor_imposto_anual())

if __name__ == '__main__':
    unittest.main()