# Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor
# que recebe por hora e calcula o salário desse funcionário.
# A seguir, mostre o número e o salário do funcionário, com duas casas decimais.

funcionario = int(input())
horas_trabalhadas = int(input())
valor_hora = float(input())

salario = horas_trabalhadas * valor_hora

print(f'NUMBER = {funcionario}')
print(f'SALARY = U$ {salario:.2f}')
