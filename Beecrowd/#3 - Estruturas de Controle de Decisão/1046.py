# Leia a hora inicial e a hora final de um jogo.
# A seguir calcule a duração do jogo, sabendo que o mesmo pode começar em um dia e terminar em
# outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.

hora_inicial, hora_final = input().split()
hora_inicial = int(hora_inicial)
hora_final = int(hora_final)

if hora_final > hora_inicial:
    duracao = hora_final - hora_inicial
else:
    duracao = (24 - hora_inicial) + hora_final

print(f'O JOGO DUROU {duracao} HORA(S)')
