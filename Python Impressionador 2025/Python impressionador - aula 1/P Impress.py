import pandas
import pyautogui
# pip install pyautogui
import time
# time não precisa instalar

# ---- PRA PAUSAR UMA AUTOMAÇÃO, TEM UMA TRAVA DE SEGURANÇA
# ---- SÓ LEVAR O MOUSE PRO CANTO SUPERIOR ESQUERDO DA TELA

# pyautogui.click -> clica
# pyautogui.press -> pressionar uma tecla
# pyautogui.write -> escrever
# pyautogui..hotkey -> atalho do teclado ('ctrl', 'c')

pyautogui.PAUSE = 1
# Ele dá uma pausa fixa EM CADA comando que ele for executar
# ele muda os comandos de cima pra baixo, por isso sempre bom colocar ele no começo do código

# --PASSO 1: ACESSAR CHROME
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
# pode ser que demore pra carregar o site. então pode add um tempo a mais pra esperar
time.sleep(3)

# --PASSO 2:  CRIAR CÓDIGO PRA CAPTURAR POSIÇÃO
# agora é a posicao. cria código auxiliar
# import pyautogui
# import time
# time.sleep(5)
# print(pyautogui.position())

# --PASSO 3: LOGAR NO SITE
pyautogui.click(x=942, y=-361)
pyautogui.write('teste.teste@hotmail.com')
pyautogui.press('tab')
pyautogui.write('senhafalsa')
pyautogui.click(x=1207, y=-202)
# ou pode clicar TAB e ENTER, tanto faz

# --PASSO 4: IMPORTAR BANCO DE DADO DOS PRODUTOS
# pip install pandas
# pip install openpyxl
tabela = pandas.read_csv('produtos.csv')
# ou dá o caminho completo de onde o arq tá
# D://usuario/Lucas/Downloads/produtos.csv
# DEPOIS DE LER, PRECISA ARMAZENAR A INF QUE ELE LEU. cria uma variável com a leitura do arq
print(tabela)
# print ela para exibir no terminal o que tem na tabela
time.sleep(3)

# --PASSO 5:  CADASTRAR O PRIMEIRO PRODUTO
# -pega posicao do primeiro campo, o resto vai com tab
# -sempre que foi cadastrar mais que 1 item, entende a lógica do 1o.
# -o código do 1o é MOLO000251,Logitech,Mouse,1,25.95,6.50,
# pyautogui.click(x=952, y=-475)  # clica no primeiro campo
# pyautogui.write('MOLO000251')  # código
# pyautogui.press('tab')
# pyautogui.write('Logitech')  # marca
# pyautogui.press('tab')
# pyautogui.write('Mouse')  # tipo
# pyautogui.press('tab')
# pyautogui.write('1')  # categoria
# pyautogui.press('tab')
# pyautogui.write('25.95')  # preço unitário
# pyautogui.press('tab')
# pyautogui.write('6.50')  # custo
# pyautogui.press('tab')
# pyautogui.write('-')  # observação
# pyautogui.press('tab')
# pyautogui.press('enter')  # enviar o produto
# pyautogui.scroll(10000)
# -número + é pra cima, negativo é pra baixo
# -pode dar um scroll com número bem alto, pra ele subir e não ter dúvida de que precisa de mais ou menos

# --PASSO 6: REPETIR O PROCESSO ANTERIOR PRA CADASTRAR TODOS OS PRODUTOS
# depois de entender como faz um, adiciona ele dentro de um CORE
# executa o mesmo código para cada linha na tabela
# - linha funciona aqui pq o python chama linha de index
# - se fosse coluna, seria <for coluna in tabela.columns>
# seleciona toda estrutura e dá um TAB, ai ele endenta tudo. Tudo dentro do for precisa de endentação
for linha in tabela.index:
    # --- linha é dinâmico, não fixo. ele executa a 1a, depois a 2a, até acabar
    pyautogui.click(x=952, y=-475)
    # código
    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(str(codigo))
    pyautogui.press('tab')
    # marca
    marca = tabela.loc[linha, 'marca']
    pyautogui.write(str(marca))
    pyautogui.press('tab')
    # tipo
    tipo = tabela.loc[linha, 'tipo']
    pyautogui.write(str(tipo))
    pyautogui.press('tab')
    # categoria
    categoria = tabela.loc[linha, 'categoria']
    pyautogui.write(str(categoria))
    pyautogui.press('tab')
    # preço unitário
    preco_unitario = tabela.loc[linha, 'preco_unitario']
    pyautogui.write(str(preco_unitario))
    pyautogui.press('tab')
    # custo
    custo = tabela.loc[linha, 'custo']
    pyautogui.write(str(custo))
    pyautogui.press('tab')
    # observação
    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan':   # pode ser < > = <= >= ou != pra diferente
        pyautogui.write(obs)
    pyautogui.press('tab')
    # enviar o produto
    pyautogui.press('enter')
    pyautogui.scroll(10000)

# nan = not a number, não preenchido, valor vazio em uma base de dados
