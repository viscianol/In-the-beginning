# Ex 028
from random import randint
from time import sleep
computador = randint(0, 5)
print('O computador pensou em um número entre 0 e 5. Tente adivinhar qual é.')
num = int(input('Qual seu palpite? '))
print('Processando, calma....')
sleep(3)
if num == computador:
    print('Parabéns, você acertou!')
else:
    print('Errou, eu pensei no número {}.' .format(computador))
print('                   ')


# Ex 029
veloc = float(input('Qual velocidade você está na pista? '))
if veloc > 80.0:
    multa = (veloc - 80.0)*7
    print('Parabéns seu animal. Você foi multado em R$ {:.2f}' .format(multa))
else:
    print('AINDA BEM. ATÉ OUTRO DIA.')
print('                   ')


# Ex 030
numero = int(input('Digite um número inteiro qualquer: '))
result = numero % 2
if result == 0:
    print('O número {} é PAR.' .format(numero))
else:
    print('O número {} é IMPAR.' .format(numero))


# Ex 031
distancia = float(input('Qual a distância da sua viagem, em Km? '))
if distancia <= 200.0:
    passagem = distancia * 0.50
else:
    passagem = distancia * 0.45
print('A sua passagem custará R$ {:.2f}' .format(passagem))
print('                   ')


# Ex 032
ano = int(input('Que ano você gostaria de analisar? '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto' .format(ano))
else:
    print('O ano {} não é bissexto.' .format(ano))


# Ex 033
num1 = int(input('Escolha o 1° número: '))
num2 = int(input('Escolha o 2° número: '))
num3 = int(input('Escolha o 3° número: '))
# Verif número menor
menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
# Verif número maior
maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
print('O menor número digitado foi {} e o maior foi {} .' .format(menor, maior))


# Ex 034
salario = float(input('Digite seu salário: R$ '))
if salario >= 1250.0:
    reajuste = salario * 1.1
else:
    reajuste = salario * 1.15
print('Seu salário será reajustado para R$ {:.2f}' .format(reajuste))
print('             ')


# Ex 034 modo alternativo
salario1 = float(input('Digite o salário: R$ '))
reajuste = float(input('Digite o % de reajuste que o salário terá: '))
calculo = salario1 + (salario1 * (reajuste / 100))
print('O salário será reajustado em {} %, passando a ser R$ {:.2f}' .format(
    reajuste, calculo))


# Ex 035
reta1 = float(input('1° segmento: '))
reta2 = float(input('2° segmento: '))
reta3 = float(input('3° segmento: '))
if reta1 < reta2+reta3 and reta2 < reta1+reta3 and reta3 < reta1+reta2:
    print('Os segmentos podem formar um triângulo.')
else:
    print('Os segmentos não podem formar um triângulo.')
