# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite seu nome completo: ')).strip().split()
print(f'Prazer em te conhecer.\nSeu primeiro nome é {nome[0]}\nSeu último nome é {nome[len(nome)-1]}')