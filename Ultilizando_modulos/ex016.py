#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
#se estivesse somente import math (teria que colocar math.trun(num))

from math import trunc
num = float(input('Digite um número real: '))

print(f'O valor digitado foi {num} Sua parte inteira é {trunc(num)}')

