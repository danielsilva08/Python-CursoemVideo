#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km_percorrido = float(input('Digite quantos Km o carro percorreu: '))
dia_alugado = float(input('Digite a quantidade de dias que o carro ficou alugado: '))

valor_km = km_percorrido * 0.15
aluguel_dia = dia_alugado * 60.00


print(f'Preço apagar pelo aluguel é de R$ {valor_km + aluguel_dia:.2f}')