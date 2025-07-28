# Desenvolva um programa que pergunte a distância de uma viagem em km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

distancia = float(input('Qual a distância da viagem? '))
print(f'Você está prestes a começar uma viagem de {distancia}Km!')

if distancia <= 200:
    preco = distancia * 0.5
else:
    preco = distancia * 0.45

print(f'O preço da passagem será R${preco:.2f}.')
