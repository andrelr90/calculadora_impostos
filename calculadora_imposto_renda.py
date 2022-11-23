class CalculadoraImpostoDeRenda():
    def __init__(self, salario_mensal):
        self.salario_mensal = salario_mensal
    
    def get_faixa_imposto(self):
        pass

    def get_valor_imposto_mensal(self):
        pass

    def get_valor_imposto_anual(self):
        pass

    def calcular_impostos(self):
        self.faixa = self.get_faixa_imposto()
        self.valor = self.get_valor_imposto_mensal()
        self.valorAnual = self.get_valor_imposto_anual()
    
