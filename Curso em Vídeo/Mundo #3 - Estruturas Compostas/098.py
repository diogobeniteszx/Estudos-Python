# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: inicio, fim
# e passo e realize a contagem.
# Seu programa tem que realizar três contagens através da função criada:

# A) De 1 até 10, de 1 em 1.
# B) De 10 até 0, de 2 em 2.
# C) Uma contagem personalizada.

def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1

    if passo == 0:
        passo = 1

    print(f'Contagem de {inicio} até {fim}, de {passo} em {passo}:')

    if inicio < fim:
        for c in range(inicio, fim + 1, passo):
            print(c, end=' ')
    else:
        for c in range(inicio, fim - 1, -passo):
            print(c, end=' ')
    print('Fim!')


contador(1, 10, 1)
contador(10, 0, 2)

print('Agora é sua vez de contar!')

inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio, fim, passo)
