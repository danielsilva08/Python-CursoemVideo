#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

altura = float(input('Digite a altura da parede em mt: '))
largura = float(input('Digite a largura da parede em mt: '))
area = altura * largura
litro_tinta = area / 2
print(f'A altura digitada foi {altura}\nA largura digita foi {largura}\nO metro quadrado é {area}\nGastarei {litro_tinta} litros de tinta por metro quadrado.')

