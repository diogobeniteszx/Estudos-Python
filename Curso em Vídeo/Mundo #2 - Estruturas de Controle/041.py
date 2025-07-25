# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um
# atleta e mostre sua categoria, de acordo com a idade:

# Até 9 anos: MIRIM.
# Até 14 anos: INFANTIL.
# Até 19 anos: JUNIOR.
# Até 20 anos: SÊNIOR.
# Acima: MASTER.

from datetime import date

atual = date.today().year
ano = int(input('Ano de nascimento: '))
idade = atual - ano
print(f'O atleta tem {idade} anos.')

if idade <= 9:
    print('Classificação: Mirim!')
elif idade <= 14:
    print('Classificação: Infantil!')
elif idade <= 19:
    print('Classificação: Júnior!')
elif idade <= 25:
    print('Classificação: Sênior!')
else:
    print('Classificação: Master!')
