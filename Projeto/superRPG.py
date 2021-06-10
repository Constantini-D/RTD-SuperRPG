from random import randint


def gritar(funcao):
    def aumentar(*args, **kwargs):
        return  funcao(*args, *kwargs).upper()
    return aumentar


class Npc:

    def __init__(self, nome, life, armor, mana, inte, str):

        self.life = life
        self.armor = armor
        self.mana = mana
        self.inte = inte
        self.str = str
        self.nome = nome

    def status(self):
        print(f'O personagem {self.nome} da classe {self.classe} possui {self.life} de vida e {self.armor} de armadura')
        if self.mana == 0 and self.classe == 'Mago':
            print('o Mago está sem mana, é recomendado correr ')

    def recebeu_dano(self, sim):
        if sim:
            dano = randint(1, 10)
            total = self.life - dano
            print(f' Sofreu {dano} pontos de dano')
            if total < 0:
                print(f' O {self.classe} {self.nome} morreu ')
        else:
            print('miss!')


class Cajado:
    def __init__(self):
        print(f' o mago Usa Cajado')


class Claymor:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        print(f' o guerreiro Usa Espada de {self.tamanho} metros')


class Mago(Npc, Cajado):

    def __init__(self, nome, life, armor, mana, inte):
        self.classe = __class__.__name__
        super().__init__(nome, life, armor, mana, inte, None)
        Cajado.__init__(self)

    @gritar
    def magia(self, magia):
        return f'{magia}'


class Guerreiro(Npc, Claymor):
    def __init__(self, nome, life, armor, str, mana, tamanho):
        self.classe = __class__.__name__
        super().__init__(nome, life, armor, mana, None, str)
        Claymor.__init__(self, tamanho)


class Dragao(Npc):
    def __init__(self, nome, life, armor, str, mana, inte):
        self.classe = __class__.__name__
        super().__init__(nome, life, armor, mana, inte, str)


mago = Mago('Mithrandir', 100, 35, 0, 60)
mago.status()
mago.recebeu_dano(True)
mago.recebeu_dano(False)
print(mago.magia('fus ro dah'))
print('\n')
guerreiro = Guerreiro('Buiuia', 35, 40, 55,10, 3)
guerreiro.status()
print('\n')
dragao = Dragao('Midir', 1, 40, 55, 70, 10)
dragao.status()
dragao.recebeu_dano(True)
print('\n')

