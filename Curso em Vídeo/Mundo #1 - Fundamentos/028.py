# Escreva um programa que faça o computador "pensar" em um número inteiro entre o 0 e 5 e peça para
# o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint

computador = randint(0, 5)
palpite = int(input('Em que número eu pensei de 0 a 5? '))

if palpite == computador:
    print('Parabéns! Você acertou!')
else:
    print(f'Errou! Eu pensei no número {computador} e não no {palpite}!')
