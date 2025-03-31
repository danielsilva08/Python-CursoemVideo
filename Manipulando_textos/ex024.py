#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = str(input('Digite o nome da cidade onde voçê nasceu: ')).strip()#elimina os espaços antes e depois mais não entre as palavras
print(cidade[:5].upper() == 'SANTO')

