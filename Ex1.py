"""Classe que representa uma pessoa, com atributos privados idade,altura e nome, utilizando sets e gets para imprimir os dados """

class Pessoa:

    def __init__(self, nome, altura, idade):
        self.__nome = nome
        self.__altura = altura
        self.__idade = idade


    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        self.__nome = valor

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, valor):
        self.__altura = valor

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, valor):
        self.__idade = valor

    def imprimir(self):
        return print(f'Nome:{self.nome}, Altura:{self.altura}, Idade:{self.idade}')


p1 = Pessoa(nome='Douglas',idade=24, altura=1.81 )
p1.imprimir()
p2 = Pessoa(nome='Teste',idade=22, altura=1.61 )
p2.imprimir()