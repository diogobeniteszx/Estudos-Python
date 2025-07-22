# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

matriz = []

for l in range(3):
    linha = []
    for c in range(3):
        numero = int(input(f'Número na posição [{l}, {c}]: '))
        linha.append(numero)
    matriz.append(linha)

print()

for linha in matriz:
    for numero in linha:
        print(f'{numero:^7}', end='')
    print()
