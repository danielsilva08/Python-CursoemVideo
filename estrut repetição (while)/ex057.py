# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = 'M/F'
while sexo:
    sexo = str(input('Informe o sexo[M/F]: ')).upper()
    if sexo != 'M' and 'F':
        print('Você digitou errado. Por favor, Digite o sexo novamente.')
        
   
      

