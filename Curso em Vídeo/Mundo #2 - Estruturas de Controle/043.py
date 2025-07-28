# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu
# status, de acordo com a tabela abaixo:

# Abaixo de 18.5: Abaixo do Peso.
# Entre 18.5 e 25: Peso ideal.
# 25 até 30: Sobrepeso.
# 30 até 40: Obesidade.
# Acima de 40: Obesidade mórbida.

peso = float(input('Qual é o seu peso? '))
altura = float(input('Qual é a sua altura? '))
imc = peso / (altura ** 2)
print(f'Seu IMC é {imc:.1f}')

if imc < 18.5:
    print('Você está ABAIXO do peso normal!')
elif imc < 25:
    print('Parabéns, você está no peso normal!')
elif imc < 30:
    print('Você está com SOBREPESO!')
elif imc < 40:
    print('Você está OBESO!')
else:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')
