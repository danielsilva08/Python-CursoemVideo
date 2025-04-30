numero = 1
par = 0
impar = 0
while numero != 0:
    numero = int(input('Digite um valor: '))
    if numero != 0: # para desconsiderar o numero nulo 0 na contagem.
        if numero % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1
print(f'você digitou {par} numeros pares e {impar} numeros impares.')