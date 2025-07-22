# Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo.
# A seguir calcule a duração do jogo.

# Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

hora_inicial, minuto_inicial, hora_final, minuto_final = input().split()
hora_inicial = int(hora_inicial)
minuto_inicial = int(minuto_inicial)
hora_final = int(hora_final)
minuto_final = int(minuto_final)

tempo_inicial = hora_inicial * 60 + minuto_inicial
tempo_final = hora_final * 60 + minuto_final

if tempo_final > tempo_inicial:
    duracao = tempo_final - tempo_inicial
else:
    duracao = (24 * 60 - tempo_inicial) + tempo_final

if duracao == 0:
    duracao = 24 * 60

horas = duracao // 60
minutos = duracao % 60

print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')
