#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal #
#– 3x ou mais no cartão: 20% de juros
print('==' * 9)
print('Loja Daniel Silva')
print('==' * 9)
preco = float(input('Preço das Compras: R$ '))
print('==' * 9)
print('''FOMAS DE PAGAMENTO.
    [1] à vista dinheiro/cheque
    [2] à vista no cartão
    [3] 2x no cartão
    [4] 3x ou mais no cartão  
      ''')
opcao = int(input('Digite a opção de pagamento? '))
if opcao == 1:
    print(f'Sua compra de R${preco} vai custar R$ {preco - (preco * 10 / 100)} no final. ')
elif opcao == 2:
    print(f'Sua compra de R${preco} vai custar R$ {preco - (preco * 5 / 100)} no final. ')  
elif opcao == 3:
    totalparc = int(input('Quantas vezes? ')) 
    print(f'Sua compra de R$ {preco} será parcelada em {totalparc}x de R$ {preco / 2} SEM JUROS. ')
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totalparc = int(input('Quantas parcelas? ')) 
    parc = total / totalparc
    print(f'Sua compra será parcelada em {totalparc}x de R$ {parc} COM JUROS.\nSua compra de R$ {preco} vai custar R$ {total} ')    
  

