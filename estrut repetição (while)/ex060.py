# Faça um programa que leia um número qualquer e mostre o seu fatorial.
#from math import factorial
#num = int(input('Digite um número para\ncalcular seu fatorial: '))
#fun = factorial(num)
#print(f'O fatorial de {num} é {fun}')
num = int(input('Digite um número para\ncalcular seu fatorial: '))
contador = num
fatorial = 1
print(f'Calculando {contador}! ')
while contador > 0:
    print(f'{contador}', end='')
    print(' x ' if contador > 1 else ' = ', end='')
    fatorial = fatorial * contador
    contador = contador - 1
print(f'{fatorial}')    



