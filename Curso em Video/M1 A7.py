# Operações aritméticas
# soma, subtração, multiplicação, divisão, potência ** (ao quadrado) , divisão inteira // , resto da divisão %
# SOBRE A DIVISÃO: 5 / 2 dá 2,5. Na // é igual a 2, pq é o número inteiro resultante. Na % é igual a 1 pq o que sobre dele é o 1, antes de add o 0 pra dividir completo
# = é pra RECEBE , == é de igual

n1 = int(input('Digite um número:'))
n2 = int(input('Digite mais um número:'))
soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2
print('A soma entre {} e {} é igual a {}' .format(n1, n2, soma))
print('A subtração entre {} e {} é igual a {}' .format(n1, n2, sub))
print('A multiplicação entre {} e {} é igual a {}' .format(n1, n2, mult))
print('A divisão entre {} e {} é igual a {}' .format(n1, n2, div))

print(n1+n2)
print(n1-n2)
print(n1*n2)
print(n1/n2)
print(n1**n2)
print(n1//n2)
print(n1 % n2)

# ORDEM DE PRECEDÊNCIA, quais rodam primeiro
# no python usa () [] {}, mas em contas só usa os () e pode ter (())
# 1o resolve (), 2o resolve **, 3o resolve * / // % NA ORDEM QUE APARECER, em 4o resolve + -
# exemplos:
# 5+3*2 == 11
# 3*5+4**2 = 31 -> 4**2=16, 3*5=15, 15+16=31
# 3*(5+4)**2==243 -> (5+4)=9, 9**2=81, 3*81=243

# outra forma de potência é uma função intera: pow(4,2)=16 , pow(4,3)=16
# raiz pode ser calculado elevando à 1/2: 81**(1/2)=9 , 25**(1/2)=5  -> resolve (), dá 0,5, depois resolve a **
# raiz cubica eleva a 1/3: 127**(1/3)=5,0265256

# dá pra fazer isso com texto tbm
print('Oi'+'Olá')
print('Oi'*5)
print('='*20)

# escrever algo em X espaços e alinhar o texto nele
nome = (input('Qual seu nome?'))
# escrever nome em 20 espaços, sem alinhamento
print('Prazer em te conhecer {:20}!' .format(nome))
# escrever nome em 20 espaços, alinhado pra direita
print('Prazer em te conhecer {:>20}!' .format(nome))
# escrever nome em 20 espaços, alinhado pra esquerda
print('Prazer em te conhecer {:<20}!' .format(nome))
# escrever nome em 20 espaços, centralizado
print('Prazer em te conhecer {:^20}!' .format(nome))
# escrever nome em 20 espaços, com símbolos preenchendo os espaços em branco
print('Prazer em te conhecer {:=^20}!' .format(nome))

# modificando o texto no print
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
soma = n1+n2
mult = n1*n2
div = n1/n2
divint = n1//n2
expo = n1**n2
print('A soma vale {}, o produto vale {}, e a divisão vale {}' .format(soma, mult, div), end=" ")
    # esse end une as 2 linhas de print em uma só, e se quiser pode add alguma coisa nele
print('A div int vale {} e a potência vale {}' .format(divint, expo))

# \n quebra a linha , :.3f é limitar o campo em 3 caractéres decimais em float
print('A soma vale {}, \n o produto vale {}, \n e a divisão vale {:.3f}' .format(soma, mult, div))
print('A div int vale {} \n e a potência vale {}' .format(divint, expo))

# agora vem os desafios 5 até o 13
