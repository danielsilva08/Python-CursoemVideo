cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco')

while True:
    num = int(input('Digite um numero:'))
    if 0 <= num <= 5: 
        break 
    print(f' Voce digitou o numero {cont[num]}')
