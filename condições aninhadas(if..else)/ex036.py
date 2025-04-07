#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Qual o valor da casa ?'))
salario = float(input('Qual o seu salário ?'))
anos = int(input('Em quantos anos voçê pretende pagar ?')) 
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100

print(f'Para pagar uma casa de {casa} em {anos} anos.')
print(f'a prestação será {prestacao:.2f}')

if prestacao <= minimo:
    print(f'Emprestimo pode ser CONCEDIDO!')
else:
    print(f'Emprestimo Negado !')    
    

   