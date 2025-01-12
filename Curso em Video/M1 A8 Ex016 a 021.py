import math
import random
# Ex 016
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porção inteira é {}' .format(num, math.trunc(num)))

# Ex 017
coposto = float(input('Comprimento do cateto oposto: '))
cadjac = float(input('Comprimento do cateto adjacente: '))
print('A hipotenusa medirá {:.2f}' .format(math.hypot(coposto, cadjac)))


# Ex 018
angulo = float(input('Digite um ângulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O seno de {} é {:.2f}, o coseno é {:.2f} e a tangente é {:.2f}' .format(
    angulo, seno, cosseno, tangente))

# Ex 019
al1 = input('Primeiro aluno: ')
al2 = input('Segundo aluno: ')
al3 = input('Terceiro aluno: ')
al4 = input('Quarto aluno: ')
lista = [al1, al2, al3, al4]
# lista de coisas é sempre em []
print('O aluno escolhido foi {}' .format(random.choice(lista)))

# Ex 020
alu1 = input('Primeiro aluno: ')
alu2 = input('Segundo aluno: ')
alu3 = input('Terceiro aluno: ')
alu4 = input('Quarto aluno: ')
lista = [alu1, alu2, alu3, alu4]
random.shuffle(lista)
print('A ordem de apresentação será')
print(lista)
