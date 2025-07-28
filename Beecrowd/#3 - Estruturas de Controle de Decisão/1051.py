# Em um país imaginário denominado Lisarb, todos os habitantes ficam felizes em pagar seus impostos,
# pois sabem que nele não existem políticos corruptos e os recursos arrecadados são utilizados em
# benefício da população, sem qualquer desvio.
# A moeda deste país é o Rombus, cujo símbolo é o R$.

# Leia um valor com duas casas decimais, equivalente ao salário de uma pessoa de Lisarb.
# Em seguida, calcule e mostre o valor que esta pessoa deve pagar de Imposto de Renda, segundo a tabela abaixo.

# |         Renda              |Imposto de Renda|
# | de 0.00 a R$2000.00        |       Isento   |
# | de R$2000.01 até R$3000.00 |       8%       |
# | de R$3000.01 até R$4500.00 |       18%      |
# | acima de R$ 4500.00        |       28%      |

salario_atual = float(input())

if salario_atual <= 2000:
    print('Isento')
else:
    if salario_atual <= 3000:
        imposto = (salario_atual - 2000) * 0.08
    elif salario_atual <= 4500:
        imposto = (3000 - 2000) * 0.08 + (salario_atual - 3000) * 0.18
    else:
        imposto = (3000 - 2000) * 0.08 + (4500 - 3000) * \
            0.18 + (salario_atual - 4500) * 0.28

    print(f'R$ {imposto:.2f}')
