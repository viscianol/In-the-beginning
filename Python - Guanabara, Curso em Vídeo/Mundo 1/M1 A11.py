# Cores no terminal

# Padrão ANSI, escape sequences = \
# sempre pra representar cor começa com \033[ 'código da cor' m
# pode ser nenhum, 1, 2 ou até 3 códigos
# 1o é o style da fonte, 2o é o texto, 3o é a cor do fundo
# \033[0;33;44m  --> 0 é sem estilo

# cód pra estilo = 0 = sem estilo;  1 = negrito/bold;  4 = sublinhado/underline; 7 = negative/negativo
# cod do texto: do 30 ao 37, 30 branco, 31 vermelho, 32 verde, 33 amarelo, 34 azul, 35 magente, 36 ciano, 37 cinza
# mais que essas cores, precisa de biblioteca
# cód background: 40 a 47, = cód texto (40 bco, 41 verm, 42 vd, 43 amar, 44 az, 45 mag, 46 cia, 47 cinza)

print('\033[0;30;41mTeste de cores\033[m')
print('\033[4;33;44mTeste de cores\033[m')
print('\033[1;35;43mTeste de cores\033[m')
print('\033[0;30;42mTeste de cores\033[m')
print('\033[mTeste de cores\033[m')
print('\033[7;30mTeste de cores\033[m')

print('---' * 15)

a = 3
b = 6
print(f'Os valores são \033[1;32m{a}\033[m e \033[31m{b}\033[m')

c = 4
d = 8
print(f'Os valores são \033[4;35m{c}\033[m e \033[1;36m{d}\033[m')

print('---' * 15)


nome = 'Lucas'
print('Testando o nome do {}{}{}' .format(
    '\033[4;32;42m', nome, '\033[m'))
print(f'Testando o nome do {'\033[1;35;45m'}{nome}{'\033[m'}')
print(f'Testando o nome do {'\033[4;34m'}{nome}{'\033[m'}')
# ---->  esse é o melhor jeito, com {} pra abrir o código e {} pra fechar o código de cor

print('---' * 15)

sobrenome = 'Visciano'
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'vermelhaN': '\033[1;31;47m',
         'roxaT': '\033[4;35;40m'}
print(f'Testando sobrenome {cores['azul']}{sobrenome}{cores['limpa']} com cor')
print(f'Testando sobrenome {cores['roxaT']}{
      sobrenome}{cores['limpa']} com cor')
print(f'Testando sobrenome {cores['vermelhaN']}{
      sobrenome}{cores['limpa']} com cor')
