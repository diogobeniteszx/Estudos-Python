# Faça um programa que calcule a soma entre todos os números ímpares que são mútiplos de três e que
# se encontram no intervalo de 1 até 500.

contador = soma = 0

for c in range(1, 500, 2):
    if c % 3 == 0:
        soma += c
        contador += 1

print(f'A soma de todos os {contador} valores solicitados é {soma}')
