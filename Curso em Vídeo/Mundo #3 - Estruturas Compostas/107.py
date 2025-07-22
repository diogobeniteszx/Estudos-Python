# Crie um módulo chamado moeda.py que tenha as funçoes incorporadas aumentar(), diminuir(), dobrar() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

from pacote.modulos import moedas

preco = float(input('Digite o preço: R$'))

print(f'Aumentando 10%, temos R${moedas.aumentar(preco, 10)}')
print(f'Diminuindo 10%, temos R${moedas.diminuir(preco, 10)}')
print(f'O dobro de R${preco} é R${moedas.dobrar(preco)}')
print(f'A metade de R${preco} é R${moedas.metade(preco)}')
