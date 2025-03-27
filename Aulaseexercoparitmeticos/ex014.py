#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

celsius = float(input('Digite a temperatura em graus celsius °C: '))
fahrenheit = celsius * 1.8 + 32

print(f'A temperatura digitada em graus celsius foi: {celsius:.2f}°C \nA temperatura em graus Fahrenheit corresponde á: {fahrenheit:.2f}°F')