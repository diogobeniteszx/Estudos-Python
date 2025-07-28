# Leia um valor inteiro.
# A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto.
# As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1.
# A seguir mostre o valor lido e a relação de notas necessárias.

n = int(input())
print(n)

notas_100 = n // 100
resto = n % 100

notas_50 = resto // 50
resto %= 50

notas_20 = resto // 20
resto %= 20

notas_10 = resto // 10
resto %= 10

notas_5 = resto // 5
resto %= 5

notas_2 = resto // 2
resto %= 2

notas_1 = resto

print(f'{notas_100} nota(s) de R$ 100,00')
print(f'{notas_50} nota(s) de R$ 50,00')
print(f'{notas_20} nota(s) de R$ 20,00')
print(f'{notas_10} nota(s) de R$ 10,00')
print(f'{notas_5} nota(s) de R$ 5,00')
print(f'{notas_2} nota(s) de R$ 2,00')
print(f'{notas_1} nota(s) de R$ 1,00')
