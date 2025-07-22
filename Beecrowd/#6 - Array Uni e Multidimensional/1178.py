# Leia um valor X.
# Coloque este valor na primeira posição de um vetor N[100].
# Em cada posição subsequente de N (1 até 99), coloque a metade do valor armazenado na posição
# anterior, conforme o exemplo abaixo.
# Imprima o vetor N.

x = float(input())
n = [0] * 100
n[0] = x

for c in range(1, 100):
    n[c] = n[c - 1] / 2

for c in range(100):
    print(f'N[{c}] = {n[c]:.4f}')
