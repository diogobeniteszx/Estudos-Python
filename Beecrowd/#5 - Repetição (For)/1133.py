# Escreva um programa que leia 2 valores X e Y e que imprima todos os valores entre eles cujo resto
# da divisão dele por 5 for igual a 2 ou igual a 3.

x = int(input())
y = int(input())

if x > y:
    x, y = y, x

for c in range(x + 1, y):
    if c % 5 == 2 or c % 5 == 3:
        print(c)
