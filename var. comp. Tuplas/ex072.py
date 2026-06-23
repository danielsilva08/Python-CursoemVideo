cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco')

while True:
    num = int(input('Digite um numero de 0 a 5:'))
    if 0 <= num <= 5: 
        break 
    print('Numero invalido. Tente novamente.', end=' ')
print(f' Voce digitou o numero {cont[num]}')
