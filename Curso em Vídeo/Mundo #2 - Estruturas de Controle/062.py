# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disser que quer mostrar 0 termos.

print('Gerador de PA')

termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))

c = total = 0
adicionais = 10

while adicionais != 0:
    total += adicionais
    while c < total:
        print(f'{termo} → ', end='')
        termo += razao
        c += 1
    print('Pausa')
    adicionais = int(input('Quantos termos você quer mostrar a mais? '))

print(f'Progressão finalizada com {total} termos mostrados')
