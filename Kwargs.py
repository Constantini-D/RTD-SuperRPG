'''def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa} é {cor}')


cores_favoritas(marcos='verde', julia='amarelo')
import math

def area(r):
    return math.pi*(r**2)

# map recebe 2 paramentos: primeiro é a função e o segundo um interável.
raios = [2, 3, 4, 5, 6, 7, 8]
areas= map(area,raios)
print(list(areas))

# map com lambda
print(list(map(lambda r: math.pi*(r**4), raios)))

'''


cidades = [('berlim', 29), ('amparo',32)]
print(type(cidades))
print(cidades[1])