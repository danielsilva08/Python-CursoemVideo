#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame
pygame.init() #inicia a bilioteca do pygame
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait #Espera o evento terminar para encerrar o programa ou seja espera a musica terminar.