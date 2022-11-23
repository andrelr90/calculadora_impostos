class CalculadoraImpostoDeRenda():    
    LIMITES_E_PORCENTAGENS = [
        (22847.76, 0),
        (33919.80, 0.075),
        (45012.60, 0.15),
        (55.976,16, 0.225),
        (float("inf"), 0.275)
    ]
    
    def __init__(self, salario_mensal, ganha_decimo_terceiro):
        if (salario_mensal < 0):
            raise Exception("Salário deve ser maior que zero.")

        self.salario_mensal = salario_mensal
        self.ganha_decimo_terceiro = ganha_decimo_terceiro
    
    def get_porcentagem_imposto(self):
        for limite, porcentagem in LIMITES_E_VALORES:
            if self.salario_mensal <= limite:
                return porcentagem

    def get_valor_imposto_anual(self):
        if self.ganha_decimo_terceiro:
            salario_anual = 13 * self.salario_mensal
        else:
            salario_anual = 12 * self.salario_mensal
        return self.get_porcentagem_imposto(salario_anual) * salario_anual

    def get_faixa_textual(self):
        _, porcentagem = self.get_porcentagem_imposto()
        if porcentagem == 0:
            return "Isento"
        return str(porcentagem*100) + '%'
    