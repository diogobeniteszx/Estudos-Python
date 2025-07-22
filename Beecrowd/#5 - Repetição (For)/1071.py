# Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números impares entre eles.

x = int(input())
y = int(input())

soma = 0

if x > y:
    x, y = y, x

for c in range(x + 1, y):
    if c % 2 != 0:
        soma += c

print(soma)
