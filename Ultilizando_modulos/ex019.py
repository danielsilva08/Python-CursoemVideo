#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice

lista = ['Daniel', 'Rodrigo', 'Igor', 'Maria']
escolha = choice(lista) #Randon choice para ecolher um nome na lista.
print(f' O aluno escolhido para apagar a lousa foi ! {escolha}.')
