# Crie um programa onde 4 jogadores jogam um dado e tenham resultados aleátorios.
# Guarde esses resultados em um dicionário.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from operator import itemgetter

jogo = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)
}

print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('\nRanking dos jogadores:')
for i, v in enumerate(ranking, start=1):
    print(f'{i}° lugar: {v[0]} com {v[1]}')
