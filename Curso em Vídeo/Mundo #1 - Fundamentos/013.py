# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Qual é o salário do funcionário? R$'))
novo_salario = salario * 1.15

print(f'Um funcionário que ganhava R$ {salario:.2f}, com 15% de aumento, passa a receber R$ {novo_salario:.2f}.')
