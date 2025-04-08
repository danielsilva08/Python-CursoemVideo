#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
      [1] Para base BINÁRIA.
      [2] Para base OCTAL.
      [3] Para base HEXADECIMAL.''')
opcao = int(input('Digite a opção: '))

if opcao == 1:
    print(f'{num} Convertido para BINÁRIO é {bin(num)[2:]}') #[2:] para aparecer somente apartir da segunda casa decimal.
elif opcao == 2:
    print(f'{num} Convertido para OCTAL é {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} Convertido para HEXADECIMAL é{hex(num)[2:]}')
else:
    print('Opção inválida. Tente novamente!')    


