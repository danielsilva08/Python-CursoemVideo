#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metro = float(input('Digite uma valor em metros:'))
cent = metro * 100 
mil = metro * 10000
print(f'O valor do metro em centímetro é {cent} \nE o valor do metro em milímentro é {mil}')
