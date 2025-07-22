# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(*valores):
    print('Analisando os valores passados...')

    maior = 0

    for v in valores:
        print(v, end=' ')
        if v > maior:
            maior = v

    print(f'Foram informados {len(valores)} valores ao todo')
    print(f'O maior valor informado foi {maior}')
    print()


maior(1, 2, 4, 3)
maior()
