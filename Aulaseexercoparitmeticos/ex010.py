#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#{:.2f} Ponto fluante 2 casa decimais depois da virgula tipo de formatação

real = float(input('Quanto dinheiro voçe tem na carteira? R$ '))
dolar = real / 5.70
euro = real / 6.15
print(f'Com R$ {real:.2f} real, você pode comprar U$$ {dolar:.2f} dólares e € {euro:.2f} euros.')