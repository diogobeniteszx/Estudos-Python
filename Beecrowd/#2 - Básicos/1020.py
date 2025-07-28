# Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe em anos, meses e dias.

# Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias.
# Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360 ou 364.
# Este é apenas um exercício com objetivo de testar raciocínio matemático simples.

total_dias = int(input())

anos = total_dias // 365
resto_dias = total_dias % 365

meses = resto_dias // 30
dias = resto_dias % 30

print(f'{anos} ano(s)')
print(f'{meses} mes(es)')
print(f'{dias} dia(s)')
