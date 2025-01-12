# Aula de módulos
# comando IMPORT e a biblioteca que vc quer buscar  -> importa tudo da biblioteca
# import bebida
# mas dá pra importar um pedaço deles só:
# from bebida import cerveja

# OS IMPORTs SEMPRE FICARÃO NO INÍCIO DO ARQUIVO

# uma biblio mto usada é a math, com várias fórmulas matemáticas e afins
# dentro dela tem ceil (arredond p cima), floor(arred pra baixo), trunc (corta casa decimal), pow (potência), sqrt (raiz quadrada), etc
# ou vc importa tudo: import math
# ou só puxa o q vc quer: from math import sqrt
# ou mais que uma função: from math import sqrt , floor, ceil

import random
from math import sqrt, floor
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz do número {} é igual a {}' .format(num, raiz))
print('A raiz do número {} é igual a {:.2f}' .format(num, raiz))
print('A raiz do número {} é igual a {}' .format(num, math.ceil(raiz)))
print('A raiz do número {} é igual a {}' .format(num, math.floor(raiz)))
# quando importa tudo, precisa referenciar com biblio.função()

# se importar SÓ UMA FUNÇÃO, não precisa referenciar biblio e função, apenas a função em si
# a VIRGULA permite importar mais que um elemento da biblio
num2 = int(input('Digite outro número: '))
raiz2 = sqrt(num2)
print('A raiz do número {} é igual a {}' .format(num2, floor(raiz2)))

num3 = random.random()
num4 = random.randint(1, 15)
print(num3, num4)
