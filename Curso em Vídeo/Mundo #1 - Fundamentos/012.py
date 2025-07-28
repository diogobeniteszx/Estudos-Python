# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

produto = float(input('Qual o preço do produto? R$'))
desconto = produto * 0.95

print(f'O produto que custava R$ {produto:.2f}, na promoção com desconto de 5% vai custar R$ {desconto:.2f}.')
