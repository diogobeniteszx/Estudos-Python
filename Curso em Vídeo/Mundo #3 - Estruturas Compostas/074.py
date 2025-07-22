# Crie um programa que vai gerar cinco número aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

valores = (
    randint(1, 10),
    randint(1, 10),
    randint(1, 10),
    randint(1, 10),
    randint(1, 10)
)

print('Valores sorteados:', end=' ')
for valor in valores:
    print(valor, end=' ')

print(f'\nMaior valor sorteado: {max(valores)}')
print(f'Menor valor sorteado: {min(valores)}')
