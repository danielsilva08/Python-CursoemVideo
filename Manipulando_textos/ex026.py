#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).strip().upper()#elimina os espaços antes do inicio e do fim mais não entre as palavras/upper le as letra tanto na maiuscula
print(f'A letra (A) Aparece {frase.count('A')} vezes na frase.\nA primeira letra (A) apareceu na posição {frase.find('A')+1}\nA letra (A) aparece na ultima vez na posição {frase.rfind('A')-1} ')
#.count() conta quantas vezes a letra aparece na frase
#.find()em qual posição aparece a letra primeira vez
.rfind() em qual posição a letra aprece pela ultima vez. r de right procure do lado direito