# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# MEDIA MENOR QUE 5 REPROVADO / MEDIA 5 E 6.9 EM RECUPERAÇÃO / MEDIA MAIOR QUE 7 APROVADO.
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2

if media <= 5:
    print(f'Tirando {nota1} e {nota2}, a média do aluno é {media}\nAluno reprovado!!')
elif media >= 5 and media <= 6.9:
    print(f'Tirando {nota1} e {nota2}, a média do aluno é {media}\nAluno em recuperação!!')
elif media >= 7:
      print(f'Tirando {nota1} e {nota2}, a média do aluno é {media}\nAluno aprovado!!')      