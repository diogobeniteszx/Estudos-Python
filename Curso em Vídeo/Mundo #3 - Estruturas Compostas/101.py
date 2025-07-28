# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de
# nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO,
# OPCIONAL ou OBRIGATÓRIO nas eleições.

def voto(ano):
    atual = 2025
    idade = atual - ano

    if idade < 16:
        return f'Com {idade} anos: Não vota!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: Voto opcional!'
    else:
        return f'Com {idade} anos: Voto obrigatório!'


nascimento = int(input('Em que ano você nasceu? '))
print(voto(nascimento))
