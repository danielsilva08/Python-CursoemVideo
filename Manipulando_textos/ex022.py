#Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.
nome = str(input('Digite o seu nome completo: ')).strip()#elimina os espaços antes e depois mais não entre as palavras
print(f'Analisando seu nome... \nSeu nome em maiúscula é {nome.upper()} \nSeu nome em minúscula é {nome.lower()}\nSeu nome tem ao todo {len(nome)-nome.count(' ')}')

separa = nome.split()
print(f'Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])}')      

#-nome.count(' ')para eliminar a contagen dos espaços entre o nome
#nome.find(' ') encontre o primeiro espaço e conte. seria uma outra opçao de contar somente o primeiro nome sem a nescessidade de fazer a variavel separa.


