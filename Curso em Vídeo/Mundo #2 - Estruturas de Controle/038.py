# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:

# O primeiro valor é maior.
# O segundo valor é maior.
# Não existe valor maior, os dois sao iguais.

valor1 = int(input('Número 1: '))
valor2 = int(input('Número 2: '))

if valor1 > valor2:
    print('O primeiro valor é maior!')
elif valor1 < valor2:
    print('O segundo valor é maior!')
else:
    print('Os valores são iguais!')
