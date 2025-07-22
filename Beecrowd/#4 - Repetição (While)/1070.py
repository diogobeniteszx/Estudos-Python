# Leia um valor inteiro X.
# Em seguida apresente os 6 valores ímpares consecutivos a partir de X, um valor por linha,
# inclusive o X ser for o caso.

n = int(input())

if n % 2 == 0:
    inicio = n + 1
else:
    inicio = n

c = 0
while c < 6:
    print(inicio + 2 * c)
    c += 1
