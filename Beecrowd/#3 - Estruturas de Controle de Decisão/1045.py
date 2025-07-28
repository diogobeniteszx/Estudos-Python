# Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente, de modo que o lado A
# representa o maior dos 3 lados.
# A seguir, determine o tipo de triângulo que estes três lados formam, com base nos seguintes casos,
# sempre escrevendo uma mensagem adequada:

# se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
# se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO
# se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO
# se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO
# se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
# se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES

a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

if a < b:
    a, b = b, a
if a < c:
    a, c = c, a
if b > c:
    b, c = c, b

if b + c <= a:
    print('NAO FORMA TRIANGULO')
else:
    if b ** 2 + c ** 2 == a ** 2:
        print('TRIANGULO RETANGULO')
    if b ** 2 + c ** 2 < a ** 2:
        print('TRIANGULO OBTUSANGULO')
    if b ** 2 + c ** 2 > a ** 2:
        print('TRIANGULO ACUTANGULO')
    if a == b == c:
        print('TRIANGULO EQUILATERO')
    elif a == b or a == c or b == c:
        print('TRIANGULO ISOSCELES')
