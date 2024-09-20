class Empregado:
    def __init__(self, nome: str):
        self.nome = nome
        self.salario_base = 1500
        self.salario = 0
        self.bonus = 0
        self.comissao = 0

    def calcular_salario(self):
        raise NotImplementedError("Este método deve ser implementado pelas subclasses.")

    def obter_salario(self):
        return f"{self.nome} recebe {self.salario}R$"

class Gerente(Empregado):
    def definir_lucro_empresa(self, lucro: float):
        self.lucro = lucro
    def calcular_bonus(self):
        self.bonus = self.lucro * 0.05
    def calcular_salario(self):
        self.calcular_bonus()
        self.salario = self.salario_base + self.bonus

    def obter_salario(self):
        return f"{self.nome} é gerente e recebe {self.salario}R$"


class Vendedor(Empregado):
    def definir_venda(self, venda: float):
        self.venda = venda
    
    def calcular_comissao(self):
        self.comissao = self.venda * 0.02
    
    def calcular_salario(self):
        self.calcular_comissao()
        self.salario = self.salario_base + self.comissao
    
    def obter_salario(self):
        return f"{self.nome} é vendedor e recebe {self.salario}R$"


fred = Gerente("Fred")
fred.definir_lucro_empresa(100000)
fred.calcular_salario()
print(fred.obter_salario())

luis = Vendedor("Luis")
luis.definir_venda(10000)
luis.calcular_salario()
print(luis.obter_salario())
