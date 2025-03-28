while True:
    username = input('Digite seu nome ?')
    if username != 'neo':
        print('nunca nem vi')
        continue

    senha = input('Qual a sua senha ?')
    if senha == '1234':
        print(f'Bem vindo, {username}')
        print('Aceita uma café')
        break
     

    