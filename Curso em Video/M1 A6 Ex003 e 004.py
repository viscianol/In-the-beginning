# somar 2 valores
num1 = int(input('Digite o 1o valor:'))
num2 = int(input('Digite o 2o valor:'))
soma = num1 + num2
print('A soma dos 2 valores é igual a {}' .format(soma))
print('A soma dos números {} e {} é igual à {}' .format(num1, num2, soma))


# abrir os tipos de uma variável
algo = input('Digite algo:')
print(type(algo))
print('O tipo primitivo desse valor é', type(algo))
print('É alfabético?', algo.isalpha())
print('É numérico?', algo.isnumeric())
print('É só espaço?', algo.isspace())
print('É só minúsculo?', algo.islower())