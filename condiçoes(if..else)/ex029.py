#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = int(input('Qual a velocidade atual do carro? '))
if velocidade <= 80:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    multa = (velocidade - 80) * 7 
    print(f'MULTADO Você excedeu o limite de velocidade que é 80km/h\nVocê deve pagar uma multa de {multa:.2f}\nTenha um bom dia! Dirija com segurança!') 
      

