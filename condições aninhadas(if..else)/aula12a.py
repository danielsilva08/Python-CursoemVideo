#estruturas condicionais aninhadas, usando os comandos if.. elif.. else 
  #Estrutura Aninhada
nome = str(input('Qual o seu nome? '))

if nome == 'Daniel':
    print('Que nome Bonito')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Claudia':
    print('Que nome popular no Brasil')    
elif nome in 'Ana Janaina Jéssica':
    print('Bom nome feminino') 
else:
    print('seu nome é bem normal.')  
print(f'Tenha um bom dia, {nome} !')         
