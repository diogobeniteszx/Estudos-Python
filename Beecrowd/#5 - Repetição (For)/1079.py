# Leia 1 valor inteiro N, que representa o número de casos de teste que vem a seguir.
# Cada caso de teste consiste de 3 valores reais, cada um deles com uma casa decimal.
# Apresente a média ponderada para cada um destes conjuntos de 3 valores, sendo que o primeiro valor
# tem peso 2, o segundo valor tem peso 3 e o terceiro valor tem peso 5.

n = int(input())

for _ in range(n):
    nota1, nota2, nota3 = map(float, input().split())

    media = (nota1 * 2 + nota2 * 3 + nota3 * 5) / 10
    print(f'{media:.1f}')
