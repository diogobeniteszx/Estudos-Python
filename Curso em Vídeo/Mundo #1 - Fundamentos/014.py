# Escreva um programa que converta uma temperatura digitada em °C e converta para °F.

celsius = float(input('Informe a temperatura em °C: '))
fahrenheit = (9 * celsius) / 5 + 32

print(f'A temperatura de {celsius}°C corresponde a {fahrenheit:.1f}°F!')
