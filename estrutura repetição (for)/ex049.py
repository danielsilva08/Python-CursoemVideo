#Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
numero = int(input('Digite um número para ver a sua tabuada: '))
for c in range(0, 11):
    soma = numero * c
    print(f'{numero} x {c} = {soma} ')