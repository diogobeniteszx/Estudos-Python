# Adicione ao modulo moeda.py criado nos desafios anteriores, uma função chamada resumir(), que
# mostra na tela algumas informações geradas pelas funções que ja temos no módulo criado até aqui.

from pacote.modulos import moedas

preco = float(input('Digite o preço: R$'))

moedas.resumir(preco)
