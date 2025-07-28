# A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:

# |     Salário       |Percentual de Reajuste|
# | 0 - 400.00        |          15%         |
# | 400.01 - 800.00   |          12%         |
# | 800.01 - 1200.00  |          10%         |
# | 1200.01 - 2000.00 |          7%          |
# | Acima de 2000.00  |          4%          |

# Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste
# ganho e o índice reajustado, em percentual.

salario_atual = float(input())

if salario_atual <= 400.00:
    percentual_reajuste = 15
elif salario_atual <= 800.00:
    percentual_reajuste = 12
elif salario_atual <= 1200.00:
    percentual_reajuste = 10
elif salario_atual <= 2000.00:
    percentual_reajuste = 7
else:
    percentual_reajuste = 4

valor_reajuste = salario_atual * percentual_reajuste / 100
novo_salario = salario_atual + valor_reajuste

print(f'Novo salario: {novo_salario:.2f}')
print(f'Reajuste ganho: {valor_reajuste:.2f}')
print(f'Em percentual: {percentual_reajuste} %')
