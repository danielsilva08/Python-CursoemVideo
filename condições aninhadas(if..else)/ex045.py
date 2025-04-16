#Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas Opções:
      [0] Pedra
      [1] Papel
      [2] Tesoura''')
jogador = int(input('Qual é a sua jogada? '))
print('-=' * 14)
print(f'O computador escolheu {itens[computador]}')
print(f'Voçê escolheu {itens[jogador]}')
print('-=' * 14)

if computador == 0: #Jogou pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('VOCÊ GANHOU!')
    elif jogador == 2:
        print('COMPUTADOR GANHOU!')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1: #Jogou papel
    if jogador == 0:
        print('COMPUTADOR GANHOU!')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('VOCÊ GANHOU!')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2:#Jogou tesoura
    if jogador == 0:
        print('VOCÊ GANHOU!')
    elif jogador == 1:
        print('COMPUTADOR GANHOU!')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
            