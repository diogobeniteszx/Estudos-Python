# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar.
# No final, mostre:

# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.
# C) Qual é o nome do produto mais barato.

total = mais1000 = menor = cont = 0
barato = ''

while True:
    nome = input('Nome do Produto: ')
    preco = float(input('Preço: R$ '))
    cont += 1
    total += preco

    if preco > 1000:
        mais1000 += 1

    if cont == 1 or preco < menor:
        menor = preco
        barato = nome

    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0]

    if continuar == 'N':
        break

print(f'O total da compra foi R${total:.2f}')
print(f'Temos {mais1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
