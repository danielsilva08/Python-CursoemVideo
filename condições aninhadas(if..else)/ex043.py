#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#– IMC abaixo de 18,5: Abaixo do Peso
#– Entre 18,5 e 25: Peso Ideal
#– 25 até 30: Sobrepeso
#– 30 até 40: Obesidade
#– Acima de 40: Obesidade Mórbida

peso = float(input('Qual o seu peso? (Kg) '))
altura = float(input('Qual a sua altura? (m) '))
imc = peso / (altura * altura)
print(f'O IMC desta pessoa é {imc:.1f}')
if imc <= 18.5:
    print('Você está ABAIXO DO PESO normal')
elif imc >= 18.5 and imc <= 25:
    print('Você está COM O PESO ideal')
elif imc > 25 and imc <= 30:
    print('Você está COM SOBREPESO') 
elif imc > 30 and imc <= 40: 
    print('Você está COM OBESIDADE') 
else:
    print('Você está COM OBESIDADE MÓRBIDA. CUIDADO!!')    

