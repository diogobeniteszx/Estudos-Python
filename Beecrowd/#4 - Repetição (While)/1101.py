# Leia um conjunto não determinado de pares de valores M e N (parar quando algum dos valores for menor ou igual a zero).
# Para cada par lido, mostre a sequência do menor até o maior e a soma dos inteiros consecutivos
# entre eles (incluindo o N e M).

while True:
    m, n = map(int, input().split())

    if m <= 0 or n <= 0:
        break

    if m > n:
        m, n = n, m

    atual = m
    soma = 0

    while atual <= n:
        print(atual, end=' ')
        soma += atual
        atual += 1

    print(f'Sum={soma}')
