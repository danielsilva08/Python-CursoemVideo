#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

valor_produto = float(input('Digite o valor do produto: '))
preco_comdesconto = valor_produto - (valor_produto* 5 / 100 )  
print(f'O valor do produto é R$ {valor_produto} com 5% de desconto R$ {preco_comdesconto:.2f}')