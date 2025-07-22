# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

# Se ele ainda vai se alistar ao servio militar.
# Se é a hora de se alistar.
# Se já passou do tempo do alistamento.

# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

atual = date.today().year
ano = int(input('Ano de nascimento: '))
idade = atual - ano

if idade < 18:
    faltam = 18 - idade
    print(f'Ainda faltam {faltam} anos para o alistamento.')
    print(f'Seu alistamento será em {ano + 18}.')
elif idade > 18:
    passou = idade - 18
    print(f'Quem nasceu em {ano} tem {idade} anos em 2025.')
    print(f'Você já deveria ter se alistado há {passou} anos.')
    print(f'Seu alistamento foi em {ano + 18}.')
else:
    print(f'Quem nasceu em {ano} tem 18 anos em 2025.')
    print('Você deve se alistar IMEDIATAMENTE!')
