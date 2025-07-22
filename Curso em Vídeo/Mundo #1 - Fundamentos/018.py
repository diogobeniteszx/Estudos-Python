# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan

angulo = float(input('Digite o ângulo que você deseja: '))
rad = radians(angulo)

seno = sin(rad)
cosseno = cos(rad)
tangente = tan(rad)

print(f'O ângulo de {angulo} tem o seno de {seno:.2f}.')
print(f'O ângulo de {angulo} tem o cosseno de {cosseno:.2f}.')
print(f'O ângulo de {angulo} tem a tangente de {tangente:.2f}.')
