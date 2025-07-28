# Crie um programa que leia o nome completo de uma pessoa e mostre:

# > O nome com todas as letras maiúsculas.
# > O nome com todas as letras minúsculas.
# > Quantas letras tem ao todo (sem considerar espaços).
# > Quantas letras tem o primeiro nome.

nome = input('Digite seu nome completo: ').strip()

print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}!')
print(f'Seu nome em minúsculas é {nome.lower()}!')
print(f'Seu nome tem ao todo {len(nome) - nome.count(" ")} letras!')
print(f'Seu primeiro nome tem {nome.find(" ")} letras!')
