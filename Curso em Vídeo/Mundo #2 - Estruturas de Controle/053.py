# Crie um programa que leia uma frase qualquer e diga de ela é um palindromo, desconsiderando os espaços.

frase = input('Digite uma frase: ').strip().upper()

palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for c in range(len(junto) - 1, -1, -1):
    inverso += junto[c]

print(f'O inverso de {junto} é {inverso}')

if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
