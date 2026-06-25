#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
listagem = ('Lapis', '1,75', 'Borracha', '2,00', 'Caderno', '15,90', 'Caneta', '3,50', 'Mochila', '120,00')
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}') #^ centralizando o texto
print('-'*40)
for pos in range (0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='') #.< alinhando a esquerda e preenchendo com pontos
    else:
        print(f'R${listagem[pos]:>7}') #> alinhando a direita e preenchendo com espaços, .2f para formatar como float com 2 casas decimais