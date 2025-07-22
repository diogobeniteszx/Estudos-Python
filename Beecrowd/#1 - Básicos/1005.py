# Leia 2 valores de ponto flutuante de dupla precisão A e B, que correspondem a 2 notas de um aluno.
# A seguir, calcule a média do aluno, sabendo que a nota A tem peso 3.5 e a nota B tem peso 7.5
# (A soma dos pesos portanto é 11).

a = float(input())
b = float(input())

media = (a * 3.5 + b * 7.5) / 11

print(f'MEDIA = {media:.5f}')
