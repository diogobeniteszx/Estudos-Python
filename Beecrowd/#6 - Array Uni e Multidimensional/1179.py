# Neste problema você deverá ler 15 valores colocá-los em 2 vetores conforme estes valores forem pares ou ímpares.
# Só que o tamanho de cada um dos dois vetores é de 5 posições.
# Então, cada vez que um dos dois vetores encher, você deverá imprimir todo o vetor e utilizá-lo
# novamente para os próximos números que forem lidos.
# Terminada a leitura, deve-se imprimir o conteúdo que restou em cada um dos dois vetores,
# imprimindo primeiro os valores do vetor impar.
# Cada vetor pode ser preenchido tantas vezes quantas for necessário.

pares = []
impares = []

for _ in range(15):
    n = int(input())

    if n % 2 == 0:
        pares.append(n)
        if len(pares) == 5:
            for i in range(5):
                print(f'par[{i}] = {pares[i]}')
            pares = []
    else:
        impares.append(n)
        if len(impares) == 5:
            for i in range(5):
                print(f'impar[{i}] = {impares[i]}')
            impares = []

for i in range(len(impares)):
    print(f'impar[{i}] = {impares[i]}')

for i in range(len(pares)):
    print(f'par[{i}] = {pares[i]}')
