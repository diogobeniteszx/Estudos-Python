# Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

# Saída:
# I=1 J=7
# I=1 J=6
# I=1 J=5
# I=3 J=9
# I=3 J=8
# I=3 J=7
# ...
# I=9 J=15
# I=9 J=14
# I=9 J=13

i = 1
while i <= 9:
    j = i + 6
    while j >= i + 4:
        print(f'I={i} J={j}')
        j -= 1
    i += 2
