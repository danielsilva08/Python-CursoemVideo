#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
# Maneira tradicional sem importação
# co = float(input('Digite o comprimento cateto oposto: '))
#  ca = float(input('Digite o comprimento cateto adjacente: '))
# hi = (co ** ca + ca ** 2) ** (1/2)

from math import hypot
co = float(input('Digite o comprimento cateto oposto: '))
ca = float(input('Digite o comprimento cateto adjacente: '))
hi = hypot(ca,co)
print(f'O comprimento da hipotenusa é {hi:.2f}')