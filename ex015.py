#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dia_alugado = int(input('Digite a quantidade de dias que o carro ficou alugado: '))
km_rodado = float(input('Digite quantos Km o carro percorreu: '))

pago = (dia_alugado * 60) + (km_rodado * 0.15)
print(f'Preço apagar pelo aluguel é de R$ {pago:.2f}')