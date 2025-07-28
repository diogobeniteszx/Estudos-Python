# Faça um mini-sistema que ultilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra "FIM", o programa se encerrará.

def ajuda(msg):
    while True:
        print('SISTEMA DE AJUDA PyHELP')
        comando = input(msg)
        if comando.upper() == 'FIM':
            print('\nENCERRANDO...')
            break
        else:
            print(f'\nAcessando o manual do comando "{comando}":\n')
            help(comando)


ajuda('Função ou Biblioteca > ')
