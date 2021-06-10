class Moto:
    marcha = 0
    menor_marcha = 0
    maior_marcha = 5
    estado = False

    def __init__(self, marca, modelo, cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor

    def imprimir(self):
        print(f' A marca é: {self.marca}, modelo: {self.modelo} e a cor: {self.cor}')

    @classmethod
    def marcha_abaixo(cls):
        if cls.estado == True:
            if cls.marcha > cls.menor_marcha:
                cls.marcha = cls.marcha - 1
            else:
                print('Ação impossível de ser executada! a marcha já atingiu o mínimo')
        else:
            print('Moto está desligada! ligue-a para funcionar o comando')


    @classmethod
    def marcha_acima(cls):
        if cls.estado ==True:
            if cls.marcha < cls.maior_marcha:
                cls.marcha = cls.marcha + 1
            else:
                print('Ação impossível de ser executada! a marcha já atingiu o máximo')
        else:
            print('Moto está desligada! ligue-a para funcionar o comando')

    @staticmethod
    def mostrar_marcha():
        print(Moto.marcha)

    @classmethod
    def ligar(cls):
        if cls.estado == True:
            print('motor já está ligado')
        else:
            cls.estado =True

    @classmethod
    def desligar(cls):
        if cls.estado == False:
            print('motor já está desligado')
        else:
            cls.estado = False


moto = Moto

m1 = moto('cg', '125', 'azul')

moto.ligar()

moto.imprimir(m1)
moto.marcha_acima()
moto.marcha_acima()
moto.marcha_acima()
moto.marcha_acima()

moto.marcha_abaixo()
moto.marcha_abaixo()

moto.mostrar_marcha()