# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:

# A) Quantos números foram digitados.
# B) A lista de valores, ordenada em ordem decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

valores = []

while True:
    valor = int(input('Digite um valor: '))
    valores.append(valor)

    resposta = input('Deseja continuar? [S/N] ')
    if resposta.upper() == 'N':
        break

cont = len(valores)
print(f'Você digitou {cont} elementos.')

valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {valores}.')

if 5 in valores:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não foi encontrado na lista.')
