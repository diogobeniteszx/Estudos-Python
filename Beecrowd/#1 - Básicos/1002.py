# A fórmula para calcular a área de uma circunferência é: area = π x raio².
# Considerando para este problema que π = 3.14159:

# - Efetue o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por π.

raio = float(input())

pi = 3.14159
area = raio ** 2 * pi

print(f'A={area:.4f}')
