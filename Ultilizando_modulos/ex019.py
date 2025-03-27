#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
ang = float(input('Digite o ângulo que voçê deseja: '))
rad = math.radians(ang)
sen = math.sin(rad)
cos = math.cos(rad)
tang = math.tan(rad)

print(f'O ângulo de {ang} tem o SENO de {sen:.2f} \nO ângulo de {ang} tem o COSSENO de {cos:.2f} \n O ângulo de {ang} tem o TANGENTE de {tang:.2f}') 