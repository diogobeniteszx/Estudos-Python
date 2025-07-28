# Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo o esquema
# abaixo, da esquerda para a direita.
# Em seguida conclua qual dos animais seguintes foi escolhido, através das três palavras fornecidas.

grupo = input()
subgrupo = input()
alimentacao = input()

if grupo == 'vertebrado' and subgrupo == 'ave' and alimentacao == 'carnivoro':
    print('aguia')
elif grupo == 'vertebrado' and subgrupo == 'ave' and alimentacao == 'onivoro':
    print('pomba')
elif grupo == 'vertebrado' and subgrupo == 'mamifero' and alimentacao == 'onivoro':
    print('homem')
elif grupo == 'vertebrado' and subgrupo == 'mamifero' and alimentacao == 'herbivoro':
    print('vaca')
elif grupo == 'invertebrado' and subgrupo == 'inseto' and alimentacao == 'hematofago':
    print('pulga')
elif grupo == 'invertebrado' and subgrupo == 'inseto' and alimentacao == 'herbivoro':
    print('lagarta')
elif grupo == 'invertebrado' and subgrupo == 'anelideo' and alimentacao == 'hematofago':
    print('sanguessuga')
else:
    print('minhoca')
