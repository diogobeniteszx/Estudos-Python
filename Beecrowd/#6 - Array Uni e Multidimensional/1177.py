# Faça um programa que leia um valor T e preencha um vetor N[1000] com a sequência de valores de 0
# até T-1 repetidas vezes, conforme exemplo abaixo. Imprima o vetor N.

t = int(input())
n = []

for c in range(1000):
    resto = c % t
    n.append(resto)

for c in range(1000):
    print(f'N[{c}] = {n[c]}')
