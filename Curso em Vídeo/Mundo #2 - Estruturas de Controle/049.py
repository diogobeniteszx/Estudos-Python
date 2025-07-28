# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora ultilizando um laço for.

n = int(input('Número para ver a tabuada: '))

for c in range(1, 11):
    resultado = c * n
    print(f'{n} x {c:2} = {resultado}')
