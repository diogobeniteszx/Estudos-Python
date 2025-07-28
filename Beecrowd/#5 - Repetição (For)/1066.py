# Leia 5 valores Inteiros.
# A seguir mostre quantos valores digitados foram pares, quantos valores digitados foram ímpares,
# quantos valores digitados foram positivos e quantos valores digitados foram negativos.

pares = impares = positivos = negativos = 0

for _ in range(5):
    n = float(input())

    if n % 2 == 0:
        pares += 1
    else:
        impares += 1

    if n > 0:
        positivos += 1
    elif n < 0:
        negativos += 1

print(f'{pares} valor(es) par(es)')
print(f'{impares} valor(es) impar(es)')
print(f'{positivos} valor(es) positivo(s)')
print(f'{negativos} valor(es) negativo(s)')
