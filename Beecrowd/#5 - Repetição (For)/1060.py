# Faça um programa que leia 6 valores.
# Estes valores serão somente negativos ou positivos (desconsidere os valores nulos).
# A seguir, mostre a quantidade de valores positivos digitados.

positivos = 0

for _ in range(6):
    n = float(input())
    if n > 0:
        positivos += 1

print(f'{positivos} valores positivos')
