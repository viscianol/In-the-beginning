# mundo 2 = 5 aulas e 35 exercícios

# condições aninhadas , encaixando uma coisa na outra
# estrutura condicional dentro de uma outra estr condicional

# if, elif, else  = pra quando tiver 3 possibilidades
# elif a + pra cada outra possibilidade
# --- if é obrigatório
# --- pode usar quantos elif's quiser
# --- else é só um

edh = str(input('Qual seu comandante favorito? '))
if edh == 'Krenko':
    print('Mono red goblin...')
elif edh == 'Magda':
    print('Combeiro safado')
elif edh == 'Atraxa':
    print('Safado tbm')
else:
    print('Ah sim...')
print(f'O {edh} é um bom comandante!')

print('---' * 20)

edh2 = int(input('Qual seu comandante favorito? Escolha um número: \n 0 - Magda \n 1 - Krenko \n 2 - Krrik \n 3 - Ezuri \n 4 - outro \n Qual sua escolha? '))
if edh2 == 0:
    print('Magda é deck de combeiro safado')
elif edh2 == 1:
    print('Mono red ficha que não acaba mais')
elif edh2 == 2:
    print('Mono black combeiro safado tbm')
elif edh2 == 3:
    print('Elfo combo safado também 2')
elif edh2 == 4:
    edh3 = str(input('Então qual seu comandante favorito? '))
    print(f'Ah sim, o {edh3} é bom também')

print('---' * 20)

# desafios 36 a 45
