# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

valores = []
maior = menor = 0

for c in range(5):
    valor = int(input(f'Valor para a posição {c}: '))
    valores.append(valor)

    if c == 0:
        maior = menor = valor
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor

print(f'Você digitou os valores {valores}.')
print(f'O maior valor digitado foi {maior} nas posições:', end=' ')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end=' ')
print()

print(f'O menor valor digitado foi {menor} nas posições:', end=' ')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end=' ')
print()
