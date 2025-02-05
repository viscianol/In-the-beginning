from random import choice
import time
from datetime import date

# Ex 036
print('Bem vindo ao Financiamento da Sua Casa!')
print('Precisamos de algumas informações antes de seguirmos com o contrato: ')
casa = float(input('Qual o valor da casa que você quer comprar? R$ '))
salario = float(input('Qual seu salário? R$ '))
anos = int(input('Em quantos anos planeja pagar a casa? '))

prestacao = casa / (anos*12)
print('A prestação da casa será de R$ {:.2f}' .format(prestacao))

valormax = salario * 0.3
print('O valor máximo da parcela é de R$ {:.2f}' .format(valormax))

if prestacao <= valormax:
    print('Perfeito! Venha até minha sala para preencher os papéis!')
elif prestacao > valormax:
    print('Infelizmente não seguiremos com o contrato. O valor da prestação é maior que 30% do seu salário...')

print('---' * 20)


# Ex 037
numero = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão: 
[ 1 ] para Binário
[ 2 ] para Octal
[ 3 ] para Hexadecimal''')
baseconv = int(input('Sua opção é: '))
if baseconv == 1:
    print('{} convertido para binário é igual a {}' .format(
        numero, bin(numero)[2:]))
elif baseconv == 2:
    print('{} convertido em octal é igual a {}' .format(
        numero, oct(numero)[2:]))
elif baseconv == 3:
    print('{} convertido em hexadecimal é igual a {}' .format(
        numero, hex(numero)[2:]))
else:
    print('Opção inválida!')

print('---' * 20)

# Ex 038
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

if n1 > n2:
    print('O 1° número é maior')
elif n2 > n1:
    print('O 2° número é maior!')
elif n1 == n2:
    print('Os 2 números são iguais!')

print('---' * 20)

# Ex 039
# import time
anonasc = int(input('Que ano você nasceu? '))
atual = int(time.strftime('%Y'))
idade = atual - anonasc

if idade < 18:
    print('Ainda não está na hora de se alistar')
    print(f'Falta {18 - idade} ano(s) pra você se alistar')
    print(f'Seu alistamento será em {atual + (18-idade)}')
elif idade == 18:
    print('Tá na hora de se alistar! CORRE SEU BISONHO')
elif idade > 18:
    print('Já passou da hora de se alistar SEU BISONHO')
    print(f'Já passou {
          idade - 18} ano(s) que você devia ter se alistado... Bisonho')
    print(f'Seu alistamento foi em {atual - (idade-18)}')

print('---' * 20)

# Ex 040
nota1 = float(input('Digite a 1a nota: '))
nota2 = float(input('Digite a 2a nota: '))
media = (nota1 + nota2) / 2

if media < 5.0:
    print(f'Sua média foi de {media}')
    print('Infelizmente você foi reprovado...')
elif media >= 5.0 and media < 7.0:
    print(f'Sua média foi de {media}')
    print('Você ficou de recuperação...')
elif media >= 7.0:
    print(f'Sua média foi de {media}')
    print('Você foi aprovado!')

print('---' * 20)

# Ex 041
# from datetime import date
print('A Conf Nac de Natação precisa definir sua categoria, com base na sua idade.')
nasc2 = int(input('Qual seu ano de nascimento? '))
atual2 = date.today().year
idade2 = atual2 - nasc2
print(f'Você tem {idade2} anos')

if idade2 <= 9:
    print('Sua categoria é a MIRIM')
elif idade2 > 9 and idade2 <= 14:
    print('Sua categoria é a INFANTIL')
elif idade2 > 14 and idade2 <= 19:
    print('Sua categoria é a JUNIOR')
elif idade2 > 19 and idade2 <= 25:
    print('Sua categoria é a SÊNIOR')
elif idade2 > 25:
    print('Sua categoria é a MASTER')

print('---' * 20)

# Ex 042
reta1 = float(input('1° segmento: '))
reta2 = float(input('2° segmento: '))
reta3 = float(input('3° segmento: '))
if reta1 < reta2+reta3 and reta2 < reta1+reta3 and reta3 < reta1+reta2:
    print('Os segmentos podem formar um triângulo ', end='')
    if reta1 == reta2 == reta3:
        print('equilátero')
    elif reta1 != reta2 != reta3 != reta1:
        print('escaleno')
    else:
        print('isósceles')
else:
    print('Os segmentos não podem formar um triângulo.')

print('---' * 20)

# Ex 043
print('Calcule seu IMC!')
peso = float(input('Quantos quilos você pesa, em kg? '))
altura = int(input('Qual sua altura, em cm? '))
IMC = peso / ((altura/100) ** 2)
print('Seu IMC é igual à {:.1f}' .format(IMC))

if IMC < 18.5:
    print('Abaixo do peso')
elif IMC >= 18.5 and IMC < 25:
    print('Peso ideal')
elif IMC >= 25 and IMC < 30:
    print('Sobrepeso')
elif IMC >= 30 and IMC < 40:
    print('Obesidade')
elif IMC >= 40:
    print('Obesidade mórbida')

print('---' * 20)

# Ex 044
preco = float(input('Qual o preço do produto? R$ '))
condpgto = int(input('''Escolha a opção de pagamento desejada:
1 - à vista dinheiro
2 - à vista cartão
3 - até 2x cartão
4 - 3x ou mais no cartão
Qual sua escolha? '''))

if condpgto == 1:
    print('Tem 10% de desconto')
    valor = preco * 0.9
    print('O valor final será de R$ {:.2f}' .format(valor))
elif condpgto == 2:
    print('Tem 5% de desconto')
    valor = preco * 0.95
    print('O valor final será de R$ {:.2f}' .format(valor))
elif condpgto == 3:
    print('Preço normal do produto.')
    valorparc = preco / 2
    print('O valor final será de R$ {:.2f}, com 2 parcelas de R$ {:.2f} sem juros.' .format(
        preco, valorparc))
elif condpgto == 4:
    print('Tem 20% de juros')
    valor = preco * 1.2
    parc = int(input('Quantas parcelas? '))
    valorparc = valor / parc
    print('O valor final será de R$ {:.2f}, com {} parcelas de R$ {:.2f} com juros.' .format(
        valor, parc, valorparc))
else:
    print('Opção inválida!')

print('---' * 20)

# Ex 045
# from random import choice
print('Jo  ken  pô  !')
pc = choice(['pedra', 'papel', 'tesoura'])
jogador = str(
    input('Escolha uma opção entre Pedra Papel ou Tesoura! ')).strip()
escolha = jogador.lower()

if pc == 'pedra':
    if escolha == 'papel':
        print(f'PC: {pc} X Jogador: {escolha}')
        print('Você ganhou')
    elif escolha == 'tesoura':
        print(f'PC: {pc} X Jogador: {escolha}')
        print('Você perdeu')
    elif escolha == 'pedra':
        print(f'PC: {pc} X Jogador: {escolha}')
        print('Empatou')
    else:
        print('Jogada inválida!')

elif pc == 'papel':
    if escolha == 'tesoura':
        print(f'PC: {pc} X Jogador: {escolha}')
        print('Você ganhou')
    elif escolha == 'pedra':
        print(f'PC: {pc} X Jogador: {escolha}')
        print('Você perdeu')
    elif escolha == 'papel':
        print(f'PC: {pc} X Jogador: {escolha}')
        print('Empatou')
    else:
        print('Jogada inválida!')

elif pc == 'tesoura':
    if escolha == 'pedra':
        print(f'PC: {pc} X Jogador: {escolha}')
        print('Você ganhou')
    elif escolha == 'papel':
        print(f'PC: {pc} X Jogador: {escolha}')
        print('Você perdeu')
    elif escolha == 'tesoura':
        print(f'PC: {pc} X Jogador: {escolha}')
        print('Empatou')
    else:
        print('Opção inválida.')
