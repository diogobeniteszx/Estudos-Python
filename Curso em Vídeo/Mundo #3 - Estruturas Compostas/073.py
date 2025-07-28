# Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de
# Futebol, na ordem de colocação.
# Depois mostre:

# A) Apenas os 5 primeiros colocados.
# B) Os útimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabetica.
# D) Em que posição da tabela está o time do Corinthians.

colocados = (
    'flamengo', 'botafogo', 'palmeiras', 'bahia', 'são paulo',
    'athletico-pr', 'cruzeiro', 'internacional', 'bragantino', 'atlético-mg',
    'fortaleza', 'grêmio', 'cuiabá', 'vasco', 'juventude',
    'corinthians', 'vitória', 'atlético-go', 'criciúma', 'fluminense'
)

print('Cinco primeiros colocados:')
for time in colocados[:5]:
    print(f'- {time.title()}')

print('\nQuatro últimos colocados:')
for time in colocados[-4:]:
    print(f'- {time.title()}')

print('\nTimes em ordem alfabética:')
for time in sorted(colocados):
    print(f'- {time.title()}')

posicao_corinthians = colocados.index('corinthians') + 1
print(f'\nO Corinthians está na {posicao_corinthians}ª posição.')
