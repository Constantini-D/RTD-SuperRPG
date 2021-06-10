"""class animal (classe pai), vai passar como herança para outros animais (subclasse) suas caracteristicas como nome, especiei
A sub classe vai ter uma função com nome de 'faz_som'
"""


"""class Pais:

    def __init__(self, mensagem, relacao):
        self.mensagem = mensagem
        self.relacao = relacao

    def ler_mensagem(self):
        print(f'{self.mensagem} a relação desta classe é {self.relacao}')


class Filhos(Pais):
    def __init__(self, mensagem, relacao):
        super().__init__(mensagem, relacao)

f = Filhos("Salveee", 'Filha')

f.ler_mensagem()"""

class Computer:

    def __init__(self, ram, memoria, nome):
        self.ram = ram
        self.memoria = memoria
        self.nome = nome

    def imprimir_caracteristicas(self):
        print(f'{self.nome} tem {self.ram} GB de ram e {self.memoria} GB de memoria')

    def tipo(self):
        print(f' Este {self.nome} é um Computador ')


class Mobile(Computer):

    def __init__(self, ram, memoria, nome):
        super().__init__(ram, memoria, nome)

    def tipo(self):
        print(f' Este {self.nome} é um Mobile ')

computador = Mobile(8, 1000, 'Avell')
dispositivo = Computer(4, 120, 'Samsung')

computador.imprimir_caracteristicas()
computador.tipo()
dispositivo.imprimir_caracteristicas()
dispositivo.tipo()