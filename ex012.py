#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

valor_produto = float(input('Digite o valor do produto:R$ '))
valor_desconto = float(input('Digite o valor do desconto: '))

valor_final = valor_produto - (valor_produto * valor_desconto / 100 )  

print(f'O valor do produto é R$ {valor_produto:.2f} você digitou {valor_desconto} % de desconto. O seu valor a pagar com desconto é R$ {valor_final:.2f}')