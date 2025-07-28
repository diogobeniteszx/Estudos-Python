# Faça um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são pares e
# mostre esta informação.

pares = 0

for _ in range(5):
    n = float(input())
    if n % 2 == 0:
        pares += 1

print(f'{pares} valores pares')
