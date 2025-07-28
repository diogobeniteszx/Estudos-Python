# Faça um programa que tenha uma função chamada área(), que receba as dimenções de um terreno
# retangular(largura e comprimento) e mostre a área do terreno.

def área(l, c):
    area = l * c
    return area


largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))

print(f'Área: {área(largura, comprimento)} m²')
