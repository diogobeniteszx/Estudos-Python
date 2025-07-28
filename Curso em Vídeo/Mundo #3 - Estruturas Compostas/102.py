# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que
# indique o número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando
# se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(numero, show=False):
    """
    Calcula o fatorial de um número.

    Args:
        numero (int): O número a ser calculado.
        show (bool, optional): Se True, mostra o processo de cálculo. Defaults to False.

    Returns:
        int: O valor do fatorial calculado.
    """
    fatorial = 1

    for c in range(numero, 0, -1):
        if show:
            print(c, end='')

            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')

        fatorial *= c

    return fatorial


print(fatorial(5, show=True))
help(fatorial)
