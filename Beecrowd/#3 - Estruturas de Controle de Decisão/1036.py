# Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara.
# Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”,
# caso haja uma divisão por 0 ou raiz de numero negativo.

a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

delta = b ** 2 - 4 * a * c

if a == 0 or delta < 0:
    print('Impossivel calcular')
else:
    raiz1 = (-b + delta ** 0.5) / (2 * a)
    raiz2 = (-b - delta ** 0.5) / (2 * a)

    print(f'R1 = {raiz1:.5f}')
    print(f'R2 = {raiz2:.5f}')
