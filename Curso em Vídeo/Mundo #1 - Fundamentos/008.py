# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e mílimetros.

metros = float(input('Uma distância em metros: '))

centimetros = metros * 100
milimetros = metros * 1000

print(f'A medida de {metros}m corresponde a {centimetros:.0f}cm e {milimetros:.0f}mm.')
