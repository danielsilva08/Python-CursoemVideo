#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = 0
for pessoa in range(1, 6):
    peso = float(input(f'Qual o peso da {pessoa} Pessoa? '))
    if pessoa == 1: #se for a primeira pessoa
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior} Kg.\nO menor peso lido foi de {menor} Kg')  

  
