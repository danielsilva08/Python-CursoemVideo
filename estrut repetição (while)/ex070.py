#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.
total = totMIL = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Qual o preço: R$ '))
    cont += 1
    total += preco

    if preco > 1000:
        totMIL += 1

    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
            
    resp = ' '
    while resp not in 'SN':#Enquanto minha resposta não estiver dentro 
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp =='N':
        break
print('{:-^40}'.format('FIM DA COMPRA'))
print(f'O total da compra foi R$ {total:.2F}')
print(f'Temos {totMIL} produtos custando mais de R$ 1.000,00')
print(f'O produto mais barato foi {barato} que custa R$ {menor:.2f}')    
