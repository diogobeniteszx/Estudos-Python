# Crie um pacote que tenha dois módulos internos chamado moedas e dados.
# Tranfira todas as funções utilizadas nos DESAFIOS 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.

from pacote.modulos import moedas

preco = float(input('Digite o preço: R$'))

moedas.resumir(preco, 20, 12)
