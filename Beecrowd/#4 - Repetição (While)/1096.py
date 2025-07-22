# Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

# Saída:
# I=1 J=7
# I=1 J=6
# I=1 J=5
# I=3 J=7
# I=3 J=6
# I=3 J=5
# ...
# I=9 J=7
# I=9 J=6
# I=9 J=5

i = 1
while i <= 9:
    j = 7
    while j >= 5:
        print(f'I={i} J={j}')
        j -= 1
    i += 2
