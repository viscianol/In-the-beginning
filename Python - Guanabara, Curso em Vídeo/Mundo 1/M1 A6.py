# Aula de tipos primitivos. Tem mais que 4, mas esses são os 4 mais importantes
# Teoria #
n1 = input('Número 1:')
n2 = input('Número 2:')
soma = n1 + n2
print('A soma vale', soma)
# dá 11 pq não tratou como número, e sim como texto / string. Precisa add  INT ou FLOAT antes do input pra corrigir

num1 = int(input(('Número 1:')))
num2 = int(input(('Número 2:')))
soma2 = num1 + num2
print('A soma vale', soma2)
# aqui dá certo. o INT trata como um número inteiro

nume1 = int(input('Número 1:'))
nume2 = int(input('Número 2:'))
soma3 = nume1 + nume2
print(soma3)
# PQ AGORA DEU CERTO SEM O 3o () ??????
# AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
# num outro teste que fiz não tratou como número, e não somou. Adicionei esses 3o () e deu certo. AGORA RESOLVEU FUNCIONAR

# Os tipos são:
# int : pra números inteiros, 7 , -4 , 0 , 9875 , positivo negativo ou nulo
# float : núm reais com pontos flutuantes,  4.5 , 0.076 , -15.223 , 7.0 , o ponto chama de ponto flutuante
# O FLOAT POR PADRÃO NÃO USA VÍRGULA E SIM O PONTO !
# 7 E 7.0 VALEM A MESMA COISA TECNICAMENTE, MAS O PONTO DIFERE O TIPO DELES
# bool : valores lógicos ou booleanos, True ou False
# sempre usar com a inicial maiúscula
# str : valores caractéres, 'olá' , 'teste' , '7' , '7.5' , '' (vazia)
# pode usar '' ou "" , mas a maioria usa ''

# dois tipos de usar o print
print('O teste 1 deu', soma, ', o teste 2 deu', soma2, 'e o teste 3 deu', soma3)
print('O teste 1 deu {}, o teste 2 deu {}, e o teste 3 deu {}' .format(
    soma, soma2, soma3))
# outros lugares usam o % , mas é antigo. A forma nova de usar essa sintaxe é com o {} e .format

# PRÁTICA #
n0 = (input('Digite o 1o número:'))
print(type(n0))

n1 = int(input('Digite o número 1:'))
print(type(n1))
n2 = int(input('Digite o número 2:'))
print(type(n2))
n1en2 = n1 + n2
print('A soma deles é de {}' .format(n1en2))
print('A soma entre {} e {} é igual a {}' .format(n1, n2, n1en2))

n = input('digite algo:')
print(n .isnumeric())
# o is abre várias opções pra validação, como se fosse o bool. Se digitar A dará false, pois não é numérico. Se digitar 3 dá true.
# isalpha vale pra letras, é alphabetic aaaaaaaaaaaaaaaaaaaaaaaa
a = input('digite algo 2:')
print(a .isalpha())
