 #Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
print('=' * 23)
print('  10 TERMOS DE UMA PA  ')
print('=' * 23)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razão
for c in range(primeiro, decimo + razão, razão):
    print(f'{c}', end=' -> ')
print('ACABOU')    