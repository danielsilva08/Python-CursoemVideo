#Crie um programa que leia dois valores e mostre um menu na tela:
from time import sleep
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''
    [1] somar 
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
    ''')
    opcao = int(input('>>>>Qual a sua opção? '))
    if opcao == 1:
        somar = num1 + num2
        print(f'Valor da soma de {num1} e {num2} é  {somar}')    
    elif opcao == 2:
        multiplicar = num1 * num2
        print(f'Valor da multiplicação de {num1} e {num2} é {multiplicar}')
    elif opcao == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print(f'Valor maior entre {num1} e {num2} é {maior}')
    elif opcao == 4:
        print('Informe o número novamente. ')
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))   
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção invalida. Tente novamente.') 
        sleep(10)
    print('=-=' * 12)
print('Programa encerrado..')     


    