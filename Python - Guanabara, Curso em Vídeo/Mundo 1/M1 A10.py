# até agora os códigos foram criados de forma sequencial.
# as condições permitem que uma coisa ou outra aconteça ou não

# Condição simples: Se tem 2 possibilidades só, executa uma ou outra
# if carro.esquerda():
# bloco True
# else:  # ou seja, carro.direita()
# bloco False

# se só tem if, é uma estrutura condicional simples
# se tem else, é uma estrutura condicional composta

tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('Seu carro está novo!')
else:
    print('Seu carro está meio velho...')
print('----FIM----')

# Condição simplificada
tempo = int(input('Quantos anos tem seu carro? '))
print('carro novo' if tempo <= 3 else 'carro velho')
print('---FIM---')


# Prática
nome = str(input('Qual é seu nome? '))
if nome == 'Lucas':
    print('Que nome bonito!')
else:
    print('Que nome comum você tem...')
print('Bom dia {} !' .format(nome))

n1 = float(input('Digite a 1a nota: '))
n2 = float(input('Digite a 2a nota: '))
media = (n1+n2)/2
print('A sua média foi de {:.1f}' .format(media))
if media >= 6.0:
    print('Parabéns, você passou de ano!')
else:
    print('Infelizmente você reprovou de ano...')


# Exercícios de 28 a 35
