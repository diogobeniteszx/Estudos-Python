# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros
# elementos de uma Sequência de Fibonacci.

n = int(input("Quantos termos da sequência de Fibonacci você quer ver? "))

a = 0
b = 1
c = 0

print("Sequência de Fibonacci:")
while c < n:
    print(a, end=' ')
    a, b = b, a + b
    c += 1
