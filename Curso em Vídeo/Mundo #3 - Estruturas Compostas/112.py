# Dentro do pacote que criamos no DESAFIO 111, temos um módulo chamado dados.
# Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(), mas com
# uma validação de dados para aceitar apenas valores que sejam monetários.

from pacote.modulos import moedas, dados

preco = dados.leiaDinheiro('Digite o preço: R$')

moedas.resumir(preco, 20, 12)
