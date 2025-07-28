# Leia um valor inteiro N.
# Apresente todos os números entre 1 e 10000 que divididos por N dão resto igual a 2.

n = int(input())

c = 0
while c < 10000:
    if c % n == 2:
        print(c)
    c += 1
