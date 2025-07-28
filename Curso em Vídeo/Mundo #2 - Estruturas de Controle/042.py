# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

# Equilátero: todos os lados iguais.
# Isósceles: dois lados iguais.
# Escaleno: todos os lados diferentes.

seg1 = float(input('Primeiro segmento: '))
seg2 = float(input('Segundo segmento: '))
seg3 = float(input('Terceiro segmento: '))

if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('Os segmentos podem formar um triângulo ', end='')
    if seg1 == seg2 == seg3:
        print('equilátero!')
    elif seg1 != seg2 and seg2 != seg3 and seg1 != seg3:
        print('escaleno!')
    else:
        print('isósceles!')
else:
    print('Os segmentos NÃO podem formar um triângulo.')
