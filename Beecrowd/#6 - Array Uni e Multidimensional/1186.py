# Leia um caractere maiúsculo, que indica uma operação que deve ser realizada e uma matriz M[12][12].
# Em seguida, calcule e mostre a soma ou a média considerando somente aqueles elementos que estão
# abaixo da diagonal Secundária da matriz, conforme ilustrado abaixo (área verde).

o = input()

matriz = []
soma = 0
contador = 0

for _ in range(12):
    linha_temp = []
    for _ in range(12):
        linha_temp.append(float(input()))
    matriz.append(linha_temp)

for linha in range(12):
    for coluna in range(12):
        if linha + coluna > 11:
            soma += matriz[linha][coluna]
            contador += 1

media = soma / contador

if o == 'S':
    print(f'{soma:.1f}')
elif o == 'M':
    print(f'{media:.1f}')
