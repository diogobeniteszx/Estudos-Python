# Leia 3 valores inteiros e ordene-os em ordem crescente.
# No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na
# sequência como foram lidos.

valor1, valor2, valor3 = input().split()
valor1 = int(valor1)
valor2 = int(valor2)
valor3 = int(valor3)

original1 = valor1
original2 = valor2
original3 = valor3

if valor1 > valor2:
    valor1, valor2 = valor2, valor1
if valor1 > valor3:
    valor1, valor3 = valor3, valor1
if valor2 > valor3:
    valor2, valor3 = valor3, valor2

print(valor1)
print(valor2)
print(valor3)
print()
print(original1)
print(original2)
print(original3)
