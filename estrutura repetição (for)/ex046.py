#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
#Outra maneira de importar so o sleepO
#from time import sleep
#Daí coloca so o sleep(1) de 1 segundo
import time
for c in range(10, -1, -1):
    print(c)
    time.sleep(1)
print('BUM, BUM, POOOW !')