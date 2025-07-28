# Faça um programa que tenha uma função chamda escreva(), que receba um texto qualquer como
# parâmetro e mostre uma mensagem com tamanho adaptável.

def escreva(texto):
    tamanho = len(texto)
    print('~' * tamanho)
    print(texto)
    print('~' * tamanho)


escreva('Olá, mundo!')
