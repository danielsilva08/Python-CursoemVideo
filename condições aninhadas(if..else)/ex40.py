# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2

if media >= 5:
    print(f'Tirando {nota1} e {nota2}, a média do aluno é {media}\nAluno aprovado!!')
elif media <=5:
    print(f'Tirando {nota1} e {nota2}, a média do aluno é {media}\nAluno reprovado!!')    