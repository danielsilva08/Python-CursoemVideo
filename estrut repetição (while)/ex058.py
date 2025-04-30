#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint

computador = randint(0 ,10)
print('Sou o seu computador..Acabei de pensar em um numeor de 0 a 10.')
print('Será que você consegue adivinhar? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:    
        if jogador < computador:
            print('Mais...Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print(f'Acertou o numero era o {computador}, foram nescessarios {palpites} palpites.')        

