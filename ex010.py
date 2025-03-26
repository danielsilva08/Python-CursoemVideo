#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

real = float(input('Quanto dinheiro voçe tem na carteira R$? '))
dolar = real / 5.70

print(f'Com R$ {real:.2f} \nvocê pode comprar U$$ {dolar:.2f} dólares.')