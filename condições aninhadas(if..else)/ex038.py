#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
num1 = int(input('Primeiro numero: '))
num2 = int(input('Segundo numero: '))
if num1 > num2:
    print('O PRIMEIRO valor é maior.')
elif num2 > num1:
    print('O SEGUNDO valor é maior.')
else:
    print('Os dois valores são iguais.')
