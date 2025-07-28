# Faça um programa que leia o nome e o pesso de várias pessoas, guardando tudo em uma lista.
# No final, mostre:

# A) Quantas pesoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

pessoas = []
dados = []
maior = menor = 0

while True:
    nome = input('Nome: ')
    peso = float(input('Peso: '))

    dados.append(nome)
    dados.append(peso)

    if len(pessoas) == 0:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

    pessoas.append(dados[:])
    dados.clear()

    resposta = input('Deseja continuar? [S/N] ')
    if resposta.upper() == 'N':
        break

print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi {maior} kg. Peso de: ', end='')
for pessoa in pessoas:
    if pessoa[1] == maior:
        print(f'[{pessoa[0]}]', end=' ')
print()

print(f'O menor peso foi {menor} kg. Peso de: ', end='')
for pessoa in pessoas:
    if pessoa[1] == menor:
        print(f'[{pessoa[0]}]', end=' ')
print()
