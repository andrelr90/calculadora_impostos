LIMITES_E_PORCENTAGENS = [
    (22847.76, 0),
    (33919.80, 0.075),
    (45012.60, 0.15),
    (55976.16, 0.225),
    (float("inf"), 0.275)
]

class CalculadoraImpostoDeRenda():    
    def __init__(self, salario_mensal, ganha_decimo_terceiro):
        if (salario_mensal < 0):
            raise Exception("Salário deve ser maior que zero.")

        self.salario_mensal = salario_mensal
        self.ganha_decimo_terceiro = ganha_decimo_terceiro
    
    def _get_porcentagem_imposto(self, salario_anual):
        for limite, porcentagem in LIMITES_E_PORCENTAGENS:
            if salario_anual <= limite:
                return porcentagem

    def _get_salario_anual(self):
        if self.ganha_decimo_terceiro:
            salario_anual = 13 * self.salario_mensal
        else:
            salario_anual = 12 * self.salario_mensal
        return salario_anual

    def get_valor_imposto_anual(self):
        salario_anual = self._get_salario_anual()
        return self._get_porcentagem_imposto(salario_anual) * salario_anual

    def get_faixa_textual(self):
        porcentagem = self._get_porcentagem_imposto(self._get_salario_anual())
        if porcentagem == 0:
            return "Isento"
        return str(round(porcentagem*100, 1)) + '%'
    