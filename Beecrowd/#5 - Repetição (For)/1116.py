# Escreva um algoritmo que leia 2 números e imprima o resultado da divisão do primeiro pelo segundo.
# Caso não for possível mostre a mensagem “divisao impossivel” para os valores em questão.

n = int(input())

for _ in range(n):
    x, y = map(int, input().split())

    if y == 0:
        print('divisao impossivel')
    else:
        resultado = x / y
        print(f'{resultado:.1f}')
