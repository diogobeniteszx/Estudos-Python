# Leia um valor inteiro N.
# Apresente o quadrado de cada um dos valores pares, de 1 até N, inclusive N, se for o caso.

n = int(input())

for c in range(1, n + 1):
    if c % 2 == 0:
        quadrado = c ** 2
        print(f'{c}^2 = {quadrado}')
