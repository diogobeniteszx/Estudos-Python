# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 5.49

print(f'Com R$ {real:.2f} você pode comprar US$ {dolar:.2f}.')
