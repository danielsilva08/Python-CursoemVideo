#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for pessoa in range(1, 5):
    print(f'---- {pessoa}° Pessoa ----')
    nome = str(input('Digite um nome: ')).strip()
    idade = int(input('Digite uma idade: '))
    sexo = str(input('Digite o sexo[M/F]: ')).strip()
    somaidade = somaidade + idade
    if pessoa == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 = totmulher20 + 1
mediaidade = somaidade / 4 
print(f'A média de idade do grupo é {mediaidade} anos.')
print(f'O homen mais velho tem {maioridadehomem} anos , e o seu nome é {nomevelho}')
print(f'Ao todo são {totmulher20}, mulheres com menos de 20 anos.')       