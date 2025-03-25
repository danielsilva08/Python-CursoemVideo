#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite o número: '))
d = n * 2
t = n * 3
r = n**(1/2) 

print(f'O dobro de {n} é {d} \nO triplo de {n} é {t} \nAraiz quadrada de {n} é {r:.1f}')