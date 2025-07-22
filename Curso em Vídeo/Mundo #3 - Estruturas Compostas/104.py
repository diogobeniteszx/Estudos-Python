# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante á função
# input() do Python, só que fazendo a validação para aceitar apenas um valor númerico.

def leiaInt(msg):
    n = input(msg)
    while not n.isnumeric():
        n = input('Erro! Digite um número inteiro válido: ')
    return int(n)


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
