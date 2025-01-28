# Ex 022
nome = str(input('Qual seu nome completo? ')).strip()
print('Seu nome em maíusculo é {}' .format(nome.upper()))
print('Seu nome em minúsculo é {}' .format(nome.lower()))
print('Seu nome tem ao todo {} letras' .format(len(nome) - nome.count(' ')))
divisao = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras' .format(
    divisao[0], len(divisao[0])))


# Ex 023
numero = int(input('Digite um número de 4 dígitos: '))
unid = numero // 1 % 10
dez = numero // 10 % 10
cent = numero // 100 % 10
milh = numero // 1000 % 10
print('unidade: {}' .format(unid))
print('dezena: {}' .format(dez))
print('centena: {}' .format(cent))
print('milhar: {}' .format(milh))
# mas isso dá bug se o número não tem 4. seria bom add um IF sobre len do número digitado, mas ainda não sei fazer isso
# AQUI ELE ALUCINOU TOTAL, QUE ISSO


# Ex 024
cidade = str(input('Digite sua cidade: ')).strip()
divcidade = cidade.split()
print('santo' in divcidade[0].lower())
print('Santo' in divcidade[0].capitalize())


# Ex 025
nome2 = str(input('Digite seu nome completo: ')).strip()
print('silva' in nome2.lower())

# Ex 026
frase2 = str(input('Digite uma frase: ')).strip().lower()
print(frase2.count('a'))
print(frase2.find('a'))
print(frase2.rfind('a'))

# Ex 027
nome3 = str(input('Digite seu nome completo: ')).strip()
divnome3 = nome3.split()
print(divnome3[0])
print(divnome3[-1])
