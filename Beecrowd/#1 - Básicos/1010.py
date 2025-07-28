# Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada
# peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2.
# Após, calcule e mostre o valor a ser pago.

codigo_peca1, numero_pecas1, valor_unitario1 = input().split()
codigo_peca1 = int(codigo_peca1)
numero_pecas1 = int(numero_pecas1)
valor_unitario1 = float(valor_unitario1)

codigo_peca2, numero_pecas2, valor_unitario2 = input().split()
codigo_peca2 = int(codigo_peca2)
numero_pecas2 = int(numero_pecas2)
valor_unitario2 = float(valor_unitario2)

total_peca1 = numero_pecas1 * valor_unitario1
total_peca2 = numero_pecas2 * valor_unitario2

valor_total = total_peca1 + total_peca2

print(f'VALOR A PAGAR: R$ {valor_total:.2f}')
