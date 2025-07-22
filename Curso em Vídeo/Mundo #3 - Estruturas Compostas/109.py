# Modifique as funções que foram criadas no DESAFIO 107 para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função formatar(), desenvolvida no DESAFIO 108.

from pacote.modulos import moedas

preco = float(input('Digite o preço: R$'))

print(f'Aumentando 10%, temos {moedas.aumentar(preco, 10, True)}')
print(f'Diminuindo 10%, temos {moedas.diminuir(preco, 10, True)}')
print(f'O dobro de {moedas.formatar(preco)} é {moedas.dobrar(preco, True)}')
print(f'A metade de {moedas.formatar(preco)} é {moedas.metade(preco, True)}')
