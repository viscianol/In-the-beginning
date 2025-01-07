# Testes simples
#   print('Olá mundo')
#   print(7+4)
#   print('7'+'4')
#   print('Olá', 5)
# o + seria para mostrar uma MSG e outra MSG, não uma msg e um número
# se for mostrar uma msg e um número, a VÍRGULA funciona melhor

#   nome = 'Lucas'
#   idade = '31'
#   peso = '90'
# = é recebe , == é igual
#   print(nome, idade, peso)

# pra perguntar pra pessoa, e salvar a inf
#   nome = input('Qual seu nome?')
#   idade = input('Qual sua idade?')
#   peso = input('Qual seu peso?')
#   print(nome, idade, peso)
#   print('Olá',nome,'.Sua idade é',idade,',seu peso é',peso)

# Desafio 1
#   nome = input('Qual seu nome?')
#   print('Seja muito bem-vindo',nome,'!')
#   print('Olá',nome,'! Prazer em te conhecer!')

# Desafio 2
#   dia = input('Qual dia você nasceu?')
#   mes = input('Qual mês você nasceu?')
#   ano = input('Que ano você nasceu?')
#   print('Você nasceu no dia',dia,'de',mes,'de',ano,'. Correto?')

# Desafio 3
n1 = input('1o número:')
n2 = input('2o número:')
print(n1 + n2)
# aqui dá erro, pq tratou os números como texto. Pra corrigir, precisa add o tipo dele, int pra inteiros OU float pra decimais
# a correção seria:
num1 = int(input(('Digite 1o número:')))
num2 = int(input(('Digite 2o número:')))
soma = num1 + num2
print('A soma dos números é', soma)
