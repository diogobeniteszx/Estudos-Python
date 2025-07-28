# Leia um valor inteiro N.
# Este valor será a quantidade de valores que serão lidos em seguida.
# Para cada valor lido, mostre uma mensagem em inglês dizendo se este valor lido é par (EVEN),
# ímpar (ODD), positivo (POSITIVE) ou negativo (NEGATIVE).
# No caso do valor ser igual a zero (0), embora a descrição correta seja (EVEN NULL), pois por
# definição zero é par, seu programa deverá imprimir apenas NULL.

n = int(input())

for _ in range(n):
    x = int(input())

    if x == 0:
        print('NULL')
    else:
        if x % 2 == 0:
            paridade = 'EVEN'
        else:
            paridade = 'ODD'

        if x > 0:
            sinal = 'POSITIVE'
        else:
            sinal = 'NEGATIVE'

        print(f'{paridade} {sinal}')
