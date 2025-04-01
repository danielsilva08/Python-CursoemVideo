#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep #Para o computador demorar um pouco pra processar o resultado
computador = randint(0,5)#Faz o computador #pensar#
print('-=-'*20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar...')
print('-=-'*20)
jogador = int(input('Em que número eu pensei ? '))
print('PROCESSANDO')
sleep(2)
if jogador == computador:
    print('PARABÉNS! Voçê ganhou..')
else:
    print(f'GANHEI! Eu pensei no número {computador} e não no {jogador}')     


