# Leia 6 valores.
# Em seguida, mostre quantos destes valores digitados foram positivos.
# Na próxima linha, deve-se mostrar a média de todos os valores positivos digitados, com um dígito após o ponto decimal.

c = positivos = soma = 0

while c < 6:
    n = float(input())
    
    if n > 0:
        positivos += 1
        soma += n
    c += 1

media = soma / positivos
print(f'{positivos} valores positivos')
print(f'{media:.1f}')
