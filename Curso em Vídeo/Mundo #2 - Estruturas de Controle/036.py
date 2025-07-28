# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exeder 30% do salário ou então o empréstimo será negado.

valor = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))

prestacao = valor / (anos * 12)
limite = salario * 0.30

print(f'Para pagar uma casa de R${valor} em {anos} anos', end=' ')
print(f'a prestação será de R${prestacao:.2f}')

if prestacao <= limite:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
