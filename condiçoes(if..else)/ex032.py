#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date

ano = int(input('Que ano quer analisar? coloque 0 analisar o ano atual: '))
if ano == 0:
    ano = date.today().year # Pega o ano atual da maquina
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
# se o ano divisivel por 4 e não pode ser divisivel por 100 dif 0
# ou em tão o ano ser divisivel por 400 
     print(f'O ano {ano} é BISSEXTO.')       
else:
     print(f'O ano {ano} não é BISSEXTO.') 