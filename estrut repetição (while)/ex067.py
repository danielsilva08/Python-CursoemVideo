#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
while True:
    numero = int(input('Quer ver a tabuada de qual valor? '))
    for c in range(0, 11):
        razao = numero * c
        print(f'{numero} x {c} = {razao}')
        if numero < 0:
                break
        print('Encerrando') 

   
    