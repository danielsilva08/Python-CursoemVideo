#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input('Qual é o seu nome completo? ')).strip()#elimina os espaços antes e depois mais não entre as palavras
print(f'Seu nome tem Silva ?{'SILVA' in nome.upper()}')
