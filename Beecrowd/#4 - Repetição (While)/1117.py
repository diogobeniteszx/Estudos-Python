# Faça um programa que leia as notas referentes às duas avaliações de um aluno.
# Calcule e imprima a média semestral.
# Faça com que o algoritmo só aceite notas válidas (uma nota válida deve pertencer ao intervalo [0,10]).
# Cada nota deve ser validada separadamente.

notas_validas = 0
soma_notas = 0.0

while notas_validas < 2:
    nota = float(input())

    if 0 <= nota <= 10:
        soma_notas += nota
        notas_validas += 1
    else:
        print('nota invalida')

media = soma_notas / 2
print(f'media = {media:.2f}')
