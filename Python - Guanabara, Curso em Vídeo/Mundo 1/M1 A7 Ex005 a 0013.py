# Desafio 5
num1 = int(input('Insira um número: '))
sucess = num1 + 1
antec = num1 - 1
print('O sucessor de {} é {}, e o antecessor é o {}' .format(num1, sucess, antec))

# Desafio 6
dobro = num1**2
triplo = num1**3
raiz = num1**(1/2)
print('O dobro é {}, o triplo é {}, e a raiz quadrada é {}' .format(
    dobro, triplo, raiz))

# Desafio 7
nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
média = (nota1+nota2)/2
print('A média das notas {} e {} é de {:.2f}' .format(nota1, nota2, média))

# Desafio 8
metros = int(input('Qtd de metros: '))
centim = metros*100
milim = metros*1000
print('{} metro são {} cm e {} mm' .format(metros, centim, milim))

# Desafio 9
tabu = int(input('Insira um número: '))
print('A tabuada do {} é {},{},{},{},{},{},{},{},{} e {}' .format(tabu, tabu*1,
      tabu*2, tabu*3, tabu*4, tabu*5, tabu*6, tabu*7, tabu*8, tabu*9, tabu*10))

# Desafio 10
reais = float(input('Quantos R$ você tem?'))
dolar = reais / 3.27
print('Com R$ {:.2f} você pode comprar US$ {:.2f} / {:.2f}' .format(reais, dolar, reais/3.27))

# Desafio 11
altura = float(input('Qual a altura?'))
largura = float(input('Qual a largura?'))
metros2 = altura*largura
ltinta = metros2/2
print('Para pintar uma parede com {}m de altura e {}m de largura, com {}m 2s, precisa de {} litros de tinta / {}' .format(altura,
      largura, metros2, ltinta, (altura*largura)/2))

# Desafio 12
preco = float(input('Qual o preço do produto?'))
desconto = preco*0.95
print('5% de desconto sobre R${:.2f} ficam R${:.2f}' .format(preco, desconto))

# Desafio 13
salario = float(input('Qual seu salário?'))
aumento = salario*1.15
print('Seu salário de R${:.2f} aumentou 15%, virando R$ {:.2f}' .format(
    salario, aumento))
