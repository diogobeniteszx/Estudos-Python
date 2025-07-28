# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
# retângulo, calcule e mostre o comprimento da hipotenusa.

oposto = float(input('Comprimento do cateto oposto: '))
adjacente = float(input('Comprimento do cateto adjacente: '))

hipotenusa = (oposto ** 2 + adjacente ** 2) ** 0.5
print(f'A hipotenusa vai medir {hipotenusa:.2f}.')
