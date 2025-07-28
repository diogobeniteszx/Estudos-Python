# Neste problema você deve ler um número, indicando uma linha da matriz na qual uma operação deve
# ser realizada, um caractere maiúsculo, indicando a operação que será realizada, e todos os
# elementos de uma matriz M[12][12].
# Em seguida, calcule e mostre a soma ou a média dos elementos que estão na área verde da matriz, conforme for o caso.
# A imagem abaixo ilustra o caso da entrada do valor 2 para a linha da matriz, demonstrando os
# elementos que deverão ser considerados na operação.

l = int(input())
t = input()

matriz = []

for _ in range(12):
    linha_temp = []
    for _ in range(12):
        linha_temp.append(float(input()))
    matriz.append(linha_temp)

soma = 0
for coluna in range(12):
    soma += matriz[l][coluna]

media = soma / 12

if t == 'S':
    print(f'{soma:.1f}')
elif t == 'M':
    print(f'{media:.1f}')
