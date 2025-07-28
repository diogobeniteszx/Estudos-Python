# Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir.
# Cada caso de teste consiste de dois inteiros X e Y.
# Você deve apresentar a soma de todos os ímpares existentes entre X e Y.

n = int(input())

c = 0
while c < n:
    x, y = map(int, input().split())
    
    menor = x
    maior = y
    if x > y:
        menor, maior = maior, menor
    
    soma = 0
    numero = menor + 1
    
    while numero < maior:
        if numero % 2 != 0:
            soma += numero
        numero += 1
    
    print(soma)
    c += 1
