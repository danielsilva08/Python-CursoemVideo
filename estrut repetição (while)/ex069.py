#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.
tot18 = totH = totF20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':#enquanto a resp não estiver M ou F o sistema não deixa passar
        sexo = str(input('Sexo [M/F]')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1 
    if sexo == 'F' and idade < 20:
        totF20 += 1  

    resp = ' '
    while resp not in 'SN':#enquanto a resp não estiver em S ou N o sistema não deixa passar
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}') 
print(f'Ao todo temos {totH} homens cadastrados') 
print(f'Temos {totF20} mulheres com menos de 20 anos.')      
