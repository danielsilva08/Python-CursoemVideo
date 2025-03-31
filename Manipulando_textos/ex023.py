#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
#informe o número
#analisando o numero tal.
#unidade dezena centenda milhar

num = int(input('Infome o número 0 a 9999: '))
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10


print(f'Analizando o número {num}')
print(f'Unidade{[unidade]} Dezena{[dezena]} Centena{[centena]} Milhar{[milhar]}')