#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metro = float(input('Digite uma valor em metros:'))
cm = metro * 100 
mm = metro * 1000
print(f'O valor do metro em centímetro é {cm:.0f} cm \nE o valor do metro em milímentro é {mm:.0f} mm')
