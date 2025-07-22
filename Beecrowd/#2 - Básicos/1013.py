# Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”.

# Utilize a fórmula:
# MaiorAB = (a + b + abs(a - b)) // 2.

a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

maior_ab = (a + b + abs(a - b)) // 2
maior = (maior_ab + c + abs(maior_ab - c)) // 2

print(f'{maior} eh o maior')
