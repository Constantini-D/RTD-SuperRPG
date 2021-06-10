""" Agenda que armazena 10 pessoas, remove pessoas, busca pessoas pelo nome, imprime os nomes guardados
imprime pessoa pelo id"""


class Pessoa:

    def __init__(self, nome, altura, idade):
        self.__nome = nome.title()
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

    def armazena_pessoa(self):
        Agenda.lista[self.nome] = [self.idade, self.altura]


class Agenda:
    lista = dict()

    def __init__(self):
        self.pessoas = []

    @staticmethod
    def listar_contatos():
        return print(Agenda.lista)

    @classmethod
    def deletar(cls, nome):
        nome = nome.title()
        try:
            del cls.lista[nome]
        except:
            print(f'{nome},não encontrado ')

    @classmethod
    def buscar(cls, nome):
        try:
            nome = nome.title()
            print(nome, cls.lista[nome])
        except:
            print(f'O nome:{nome} não foi encontrado')


p1 = Pessoa('douglas', 24, 1.81)
p2 = Pessoa('ana', 23, 1.60)
p3 = Pessoa('dr.mundo', 30, 2)

p1.armazena_pessoa()
p2.armazena_pessoa()
p3.armazena_pessoa()

agenda = Agenda()

agenda.listar_contatos()
agenda.deletar('t')
agenda.buscar('ana')
agenda.listar_contatos()



# p2 = Pessoa(nome='Teste',idade=22, altura=1.61 )
