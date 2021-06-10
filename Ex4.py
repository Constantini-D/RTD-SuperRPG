"""
Class televisão
classe controle remoto aumenta o volume e muda de canais +1 ou pula pra um canal indicado
função que imprima os valores  e o canal
"""


class Televisao:

    @staticmethod
    def mostrar_volume():
        print(Controle.volume)

    @staticmethod
    def mostrar_canal():
        print(Controle.canais)


class Controle:
    canais = 0
    volume = 0

    @staticmethod
    def aumentar_volume():
        Controle.volume = Controle.volume+1


    @staticmethod
    def aumentar_canal():
        Controle.canais = Controle.canais + 1

    @staticmethod
    def diminuir_volume():
        Controle.volume = Controle.volume - 1

    @staticmethod
    def diminuir_canal():
        Controle.canais = Controle.canais - 1

    @classmethod
    def selecionar_canal(cls, canal):
        cls.canais = canal



televisao = Televisao
controle = Controle()

controle.aumentar_volume()
controle.aumentar_volume()
controle.aumentar_volume()
controle.aumentar_volume()
controle.aumentar_volume()
controle.aumentar_volume()
controle.selecionar_canal(30)
controle.aumentar_canal()

controle.diminuir_canal()
controle.diminuir_canal()
controle.diminuir_canal()
controle.diminuir_volume()

televisao.mostrar_canal()
televisao.mostrar_volume()