class Aluno:
    def __init__(self, nome: str, nota1: float, nota2: float):
        self.__nome = nome
        self.__nota1 = nota1
        self.__nota2 = nota2

    def get_nome(self):
        return self.__nome

    def get_nota1(self):
        return self.__nota1

    def get_nota2(self):
        return self.__nota2

    def set_nome(self, nome: str):
        self.__nome = nome

    def set_nota1(self, nota1: float):
        self.__nota1 = nota1

    def set_nota2(self, nota2: float):
        self.__nota2 = nota2

    def calcular_media(self):
        return (self.__nota1 + self.__nota2) / 2

    def mostrar_informacoes(self):
        return f"Nome: {self.__nome}, Nota1: {self.__nota1}, Nota2: {self.__nota2}, Média: {self.calcular_media()}"


aluno1 = Aluno("César", 7.5, 8.0)

print(aluno1.mostrar_informacoes())