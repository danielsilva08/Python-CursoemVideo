#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint

computador = randint(0 ,10)
print('Sou o seu computador..Acabei de pensar em um numeor de 0 a 10.')
print('Será que você consegue adivinhar? ')
acertou = False
jogador = 0
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    jogador = jogador + acertou
    if jogador == computador:
        acertou = True
print(f'Acertou o numero era o {computador}, foram nescessarios {jogador} palpites.')        

