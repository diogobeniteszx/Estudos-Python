# Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma
# fábrica, e informe-o expresso no formato horas:minutos:segundos.

n = int(input())

horas = n // 3600
resto_segundos = n % 3600

minutos = resto_segundos // 60
segundos_restantes = resto_segundos % 60

print(f'{horas}:{minutos}:{segundos_restantes}')
