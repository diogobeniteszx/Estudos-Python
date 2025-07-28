# Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item.
# A seguir, calcule e mostre o valor da conta a pagar.

# | CÓDIGO | ESPECIFICAÇÃO   | PREÇO |
# |   1    | Cachorro Quente | R$4.00|
# |   2    | X-Salada        | R$4.50|
# |   3    | X-Bacon         | R$5.00|
# |   4    | Torrada Simples | R$2.00|
# |   5    | Refrigerante    | R$1.50|


codigo, quantidade = input().split()
codigo = int(codigo)
quantidade = int(quantidade)

if codigo == 1:
    preco_unitario = 4.00
elif codigo == 2:
    preco_unitario = 4.50
elif codigo == 3:
    preco_unitario = 5.00
elif codigo == 4:
    preco_unitario = 2.00
elif codigo == 5:
    preco_unitario = 1.50
else:
    preco_unitario = 0.00

total = preco_unitario * quantidade

print(f'Total: R$ {total:.2f}')
