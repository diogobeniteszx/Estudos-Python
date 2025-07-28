# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre a mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = int(input('Qual a velocidade atual do carro? '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Multado! Você excedeu o limite permitido que é 80Km/h.')
    print(f'Você deve pagar uma multa de R${multa:.2f}!')
else:
    print('Tenha um bom dia! Dirija com segurança!')
