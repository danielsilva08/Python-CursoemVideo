#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
#A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
#strip() tira o espaço antes e depois da frase.
#upper() deixa maiuscula
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split() #SEPARA A FRASE EM PALAVRAS GERANDO UMA LISTA
junto = ''.join(palavras) #JUNTA AS PALAVRAS SEM ESPAÇO INTERNO em uma string
inverso = junto[::-1]
#for letra in range(len(junto) -1, -1, -1): #PARA LER A FRASE AO CONTRARIO
    #inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palídromo!')    


