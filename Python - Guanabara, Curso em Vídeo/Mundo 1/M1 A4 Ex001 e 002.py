# Ex 001
print('Olá Mundo!')

# Ex 002
nome = input('Qual seu nome?')
print('É um prazer te conhecer', nome)
print('É um prazer te conhecer, {} !' .format(nome))
# o {} te deixa adicionar/substituir pelas variáveis. então não precisa quebrar o texto com ('texto1' , variável , 'texto2'...)
idade = int(input(('Qual sua idade?')))
altura = int(input(('Qual sua altura em cm?')))
resultado1 = altura + idade

print('Sua idade mais altura é de', resultado1)
print('Seu nome é {}, sua idade é {}, e sua altura é {} cm' .format(
    nome, idade, altura))
