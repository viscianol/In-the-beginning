# Desafio 5 - ok
num1 = int(input('Insira um número: '))
sucess = num1 + 1
antec = num1 - 1
print('O sucessor de {} é {}, e o antecessor é o {}' .format(num1, sucess, antec))
print('O sucessor de {} é {}, e o antecessor é o {}' .format(
    num1, (num1+1), (num1-1)))

# Desafio 6 - ok
dobro = num1*2
triplo = num1*3
raiz = num1**(1/2)
print('O dobro é {}, o triplo é {}, e a raiz quadrada é {:.3f}' .format(
    dobro, triplo, raiz))

# Desafio 7 - ok
nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
média = (nota1+nota2)/2
print('A média das notas {} e {} é de {:.2f}' .format(nota1, nota2, média))

# Desafio 8 - ok
metros = float(input('Qtd de metros: '))
centim = metros*100
milim = metros*1000
print('{} metro são {:.0f} cm e {:.0f} mm' .format(metros, centim, milim))

# Desafio 9 - ok
tabu = int(input('Insira um número: '))
print('A tabuada do {} é {},{},{},{},{},{},{},{},{} e {}' .format(tabu, tabu*1,
      tabu*2, tabu*3, tabu*4, tabu*5, tabu*6, tabu*7, tabu*8, tabu*9, tabu*10))
print('{} x {} = {}' .format(tabu, 1, (tabu*1)))
print('{} x {} = {}' .format(tabu, 2, (tabu*2)))
print('{} x {} = {}' .format(tabu, 3, (tabu*3)))
print('{} x {} = {}' .format(tabu, 4, (tabu*4)))
print('{} x {} = {}' .format(tabu, 5, (tabu*5)))
print('{} x {} = {}' .format(tabu, 6, (tabu*6)))
print('{} x {} = {}' .format(tabu, 7, (tabu*7)))
print('{} x {} = {}' .format(tabu, 8, (tabu*8)))
print('{} x {} = {}' .format(tabu, 9, (tabu*9)))
print('{} x {} = {}' .format(tabu, 10, (tabu*10)))

# Desafio 10 - ok
reais = float(input('Quantos R$ você tem? R$ '))
dolar = reais / 3.27
print('Com R$ {:.2f} você pode comprar US$ {:.2f} / {:.2f}' .format(reais, dolar, reais/3.27))

# Desafio 11 - ok
altura = float(input('Qual a altura?'))
largura = float(input('Qual a largura?'))
metros2 = altura*largura
ltinta = metros2/2
print('Para pintar uma parede com {}m de altura e {}m de largura, com {}m2, precisa de {:.2f} litros de tinta / {:.2f}' .format(altura,
      largura, metros2, ltinta, (altura*largura)/2))

# Desafio 12 - ok
preco = float(input('Qual o preço do produto? R$ '))
desconto = preco*0.95
print('5% de desconto sobre R$ {:.2f} ficam R$ {:.2f}' .format(
    preco, desconto))

preco2 = float(input('Qual o preço do produto? R$ '))
desconto2 = float(input('Quantos % de desconto nele? '))
novopreco = preco2 - (preco2*desconto2/100)
print('{}% de desconto sobre R$ {:.2f} é igual à R$ {:.2f}' .format(
    desconto2, preco2, novopreco))

# Desafio 13 - ok
salario = float(input('Qual seu salário? R$ '))
aumento = salario*1.15
print('Seu salário de R${:.2f} aumentou 15%, virando R$ {:.2f}' .format(
    salario, aumento))

salario2 = float(input('Qual é o salário do funcionário? R$ '))
aumento2 = float(input('Quantos % de aumento terá? '))
novosal = salario2+(salario2*aumento2/100)
print('Um funcionário que ganhava R$ {:.2f}, com {}% de aumento, receberá R$ {:.2f}' .format(
    salario2, aumento2, novosal))
