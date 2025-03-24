#Crie um programa que leia lgo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

n = input('Digite algo: ')
print(f'O tipo primitivo deste valor é {type(n)}')
print(f'Só tem espaço? {n.isspace()}')
print(f'É um numero? {n.isnumeric()}')
print(f'É alfabético? {n.isalpha()}')
print(f'É alfanumerico? {n. isalnum()}')
print(f'Esá em maiúsculo? {n.isupper()}')
print(f'Está em minúsculo? {n.islower()}')
print(f'Ésta capitalizada? {n.istitle()}')
