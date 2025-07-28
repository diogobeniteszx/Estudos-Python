# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for impar, desconsidere-o.

soma = contador = 0

for c in range(6):
    valor = int(input(f'Informe o {c + 1}° valor: '))
    if valor % 2 == 0:
        soma += valor
        contador += 1

print(f'Você informou {contador} números PARES e a soma foi {soma}')
