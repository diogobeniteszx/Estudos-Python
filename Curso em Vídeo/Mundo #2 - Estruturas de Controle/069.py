# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programador deverá perguntar se o usuário quer ou não continuar.
# no final, mostre:

# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos hommens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.

maiores = homens = mulheres_novas = 0

while True:
    idade = int(input('Idade: '))
    sexo = ' '

    while sexo not in 'MF':
        sexo = input('Sexo: [M/F] ').strip().upper()[0]

    if idade >= 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_novas += 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0]

    if continuar == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {maiores}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheres_novas} mulheres com menos de 20 anos')
