# Reescreva a função leiaInt() que fizemos no DESAFIO 104, incluindo agora a posibilidadde de
# digitação de um número de tipo inválido.
# Aproveite e crie uma função leiaFloat() com a mesma funcionalidade.

def leiaInt(msg):
    while True:
        try:
            nint = int(input(msg))
        except:
            print('Erro! Digite um número inteiro válido.')
        else:
            return nint


def leiaFloat(msg):
    while True:
        try:
            nreal = float(input(msg))
        except:
            print('Erro! Digite um número inteiro válido.')
        else:
            return nreal


nint = leiaInt('Digite um número inteiro: ')
nreal = leiaFloat('Digite um número real: ')

print(f'O valor inteiro digitado foi {nint} e o real foi {nreal}')
