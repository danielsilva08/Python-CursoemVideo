#Operadores aritméticos
#Potênciação ** ou usar pow(4,3) = 64
#raiz quadrada ex. 81**(1/2) = 9.0
#raiz cubica ex. 127**(1/3) = 5.026525

#para colocar tudo na mesma linha end=' ' no espaço se quiser posso coloar qualquer caracteri ou deixar em branco mesmo.

n1 = int(input('Digite uma valor:'))
n2 = int(input('Digite outro valor:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print(f'A soma é {s} \nO produto é {m} \nE a divisão é {d:.3f}')#:.3f para colocar os numeros após a vircula f de floot ponto flutuante.
print(f'Divisão é inteira {di} \ne a potência é {e}')