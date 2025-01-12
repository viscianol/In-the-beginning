# Fatiamento : pegar pedaço de uma string
frase = 'Curso em Vídeo Python'
print(frase[9])
# em [], coloca o número do índice que vc quer
# minusculo e maiusculo não são a mesma coisa

print(frase[9:13])
# O ÚLTIMO NÃO APARECE. ISSO NÃO FAZ SENTIDOOOOOOOOOOO
# inclui o 9, vai até menos o 13

print(frase[9:21])
print(frase[9:21:2])
# print de 9 a 20, pulando de 2 em 2

print(frase[:5])
# como omitiu o começo, ele começa de 0 e vai até 4

print(frase[15:])
# mesma coisa, vai até o final da string sem ocultar o último

print(frase[9::3])
# omitiu, começa do 9, vai até o final, pulando de 3 em 3

print(frase[::2])
# omitiu começo, omitiu final, mas pulando de 2 em 2
# ou seja, do começo até o fim pulando 2 em 2


# BONUSsssssssssssssssssssssssssssssssssss
# quando tiver um texto longo, com mais de uma linha, não precisa add \n ou escrever print linha por linha
# pode colocar print e 3x '
print('''Lorem ipsum dolor sit amet,
consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco
laboris nisi ut aliquip ex ea commodo consequat''')


# Análisar string
print(len(frase))
# len é de lenght, de tamanho. conta qtos caract tem na str

print(frase.count('o'))
# conta qtas vezes aparece uma letra na str. sempre em ''

print(frase.count('o', 0, 13))
# contagem com fatiamento. conta '' entre X e Y caract

print(frase.find('deo'))
# em que momento da str começou. só onde ela começou, não mostra onde terminou

print(frase.find('Android'))
# quando digita algo que não existe, ele retorna -1. -1 = não encontrado

print('Curso' in frase)
# busca algo '' em str


# Transformação
print(frase.replace('Python', 'Android'))
# substitui algo dentro da str
# MAS ELE SÓ SUBSTITUI na função momentaneamente, A STR É IMUTÁVEL. a não ser que use uma função que atribua uma nova inf nela

print(frase.upper())
# transf tudo em maiusculo

print(frase.lower())
# transf tudo em minusculo
print(frase.lower() .find('vídeo'))
# transf em minusculo, e buscou vídeo. SE NÃO TIVESSE FEITO ISSO, não encontraria nada. Vídeo é diferente de vídeo

print(frase.capitalize())
# transf tudo em minusculo, e só a 1a letra fica maiuscula

print(frase.title())
# transf tudo em minusculo, e deixa as 1as letras maiusculas
# é o capitalize por palavra, considerando a quebra / espaços

frase2 = '  Aprendendo Python  '
print(frase2.strip())
# remove os espaços inuteis no começo e no final da str

print(frase2.rstrip())
# r é de direita. remove apenas os espaços da direita

print(frase2.lstrip())
# mesma coisa, so que agora é da l esquerda


# Divisão
print(frase.split())
# divisão da str considerando cada um dos espaços
# isso refaz os indices de todas as palavras, removendo os espaços
# gera uma lista com todas as str separadas

print('-'.join(frase))
# o join é usado pra reunir o que vc separou pro SPLIT ou que estão separadas de outro jeito
# numa frase normal, ele add o '-' na frase

# Exerc de 22 a 27
