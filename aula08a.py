#utilizando os comandos import e from/import no Python.carregar bibliotecas de funções e utilizar vários recursos adicionais nos seus programas utilizando módulos built-in e módulos externos, oferecidos no Pypi.
#math.ceil arredonta o numero para cima {math.ceil(raiz)} 
#math.floor arredonta para baixo {math.floor(raiz)}
#sqrt importa a raiz
#import math = todas as funções matematicas
#from math impot sqrt = somente a que eu desejar no caso aí somente a raiz quadrada

import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)

print(f'A raiz quadrada de {num} é igual a {raiz:.2f}')