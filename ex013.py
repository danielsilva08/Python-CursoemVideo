#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite o valor do salário: R$ '))
aumento = float(input('Digite o percentual do aumento do salário: '))
novo_salario = salario + (salario * aumento / 100)

print(f'O seu salário era R$ {salario:.2f} \nO percentual de aumento foi: {aumento:.0f} % \nO seu novo salário agora é R$ {novo_salario:.2f}')