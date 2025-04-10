 #Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('-=' * 12)
print('Analisador de Triângulos')
print('-=' * 12)

reta1 = float(input('Primeiro Segmento: '))
reta2 = float(input('Segundo Segmento: '))
reta3 = float(input('Terceiro Segmento: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print(f'Os segmentos acima PODEM FORMA UM TRIÂNGULO.')
else:
    print(f'Os segmentos acima NÃO PODEM FORMAR UM TRIÂNGULO.')        
