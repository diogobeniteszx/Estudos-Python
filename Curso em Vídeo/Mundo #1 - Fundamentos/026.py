# Faça um programa que leia uma frase pelo teclado e mostre:

# > Quantas vezes aparece a letra "a".
# > Em que posição ela aparece a primeira vez.
# > Em que posição ela aparece a útima vez.

frase = input('Digite uma frase: ').lower()

print(f'A letra "a" aparece {frase.count("a")} vezes na frase.')
print(f'A primeira letra "a" apareceu na posição {frase.find("a") + 1}.')
print(f'A última letra "a" apareceu na posição {frase.rfind("a") + 1}.')
