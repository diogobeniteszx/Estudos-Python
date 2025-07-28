# Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

# Saída:
# I=0 J=1
# I=0 J=2
# I=0 J=3
# I=0.2 J=1.2
# I=0.2 J=2.2
# I=0.2 J=3.2
# ...
# I=2 J=?
# I=2 J=?
# I=2 J=?

i = 0.0
while i <= 2.0:
    c = 1
    while c <= 3:
        j = i + c
        print(f'I={i} J={j}')
        c += 1
    i = round(i + 0.2, 1)
