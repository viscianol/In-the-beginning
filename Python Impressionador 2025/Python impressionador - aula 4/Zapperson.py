# criação de sistema
# -    # anota as telas que vc quer no sistema e todas as interações que vc quer no sistema
# --      # TELA INICIAL
# ---        # titulo: HAshzap
# ---        # botão: iniciar chat
# ----           # quando clicar no botão, abre popup/modal/alerta
# -----                # titulo: bem vindo ao zap
# -----                # caixa de texto: escreva seu nome
# -----                # botaõ: entrar no chat
# ------                    # quando clicar no botão1:
# ------                    # fechar o popup
# ------                    # sumir titulo,
# ------                    # sumir botao iniciar chat,
# -------                        # carregar chat
# -------                        # carregar campo de enviar msg (digite sua msg),
# -------                        # botão Enviar
# --------                            # quando clica no enviar,
# --------                            # envia a msg
# --------                            # limpa caixa de msg

# pra criar as coisas no python?
# -- Flash / Django: sites
# -- Kivy: app
# -- Tkinter: tela pra programas
# -- Ou o Flet pra todos
# --- com ele dá pra criar front e back end
# --- com o mesmo código vc cria site app e telas programa
# ---------- pip install flet

# ---- !!!! PRA QUE A FUNCAO PARE DE RODAR, PRECISA DIGITAR NO TERMINAL CTRL+C OU QLQ COISA DO TIPO, PRA APARECER PS D:/U/D/P

# PRA CRIAR
# 1o - importar flet
# ------ import flet as ft
# 2o - criar uma função principal para rodar o app
# ------ def main ():
# --------- # coloca as funcoes que fará
# 3o -  executar essa função com o flet
# ------ ft.app(main)

# IMPORTA
import flet as ft

# FUNÇÃO PRINCIPAÇ
# uso do def
# def nome_da_funcao(parametro):
# ---- o que essa funcao fará
# ---- passo 1
# ---- passo 2
# ---- passo 3
# ---- passo 4
# a funcao principal chama-se main

# ------- TUDO NOVO É CONSTRUIDO ANTES DE CHAMAR A FUNCAO NO CÓDIGO
# cria de baixo pra cima. Uma funçao precisa existir ANTES de chamar ela


def main(pagina):
    # titulo
    titulo = ft.Text('Zapperson')
    pagina.add(titulo)
    # ----- cria o que quer na 1a linha & adiciona isso na aplicação na 2a

    # pros usuarios se comunicar, precisa fazer um tunel de comunicacao = websocket
    # são 3 passos: cria funcao , criar tunel comunicacao pagina.pubsub, enviar msg tunel comunc alterando os cod q enviava msg
    def enviar_mensagem_tunel(mensagem):
        # executar tudo q quero q aconteca pra todos usuários
        texto = ft.Text(mensagem)
        chat.controls.append(texto)
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
        print('Clicou no botão')
        # precisa add um evento. sempre qeu funcao esta atribuida a um evento de click num botao, precisa add parametro 'evento'
        # tudo que acontecerá na pag precisa ser criado antes do botão. é a ordem das coisas
        # o botao em último considera tudo antes dele, e nao depois
        # pagina.update() é pra atualizar automaticamente o que o usuário está vendo
        # sempre que fizer algo que atualizará a tela do user, precisa do update

    def enviar_mensagem(evento):
        nome_usuario = caixa_nome.value
        texto_campo_mensagem = campo_enviar_mensagem.value
        mensagem = f'{nome_usuario}: {texto_campo_mensagem}'
        pagina.pubsub.send_all(mensagem)
        # limpa a caixa de enviar msg
        campo_enviar_mensagem.value = ''
        pagina.update()

    campo_enviar_mensagem = ft.TextField(
        label='Digite aqui sua mensagem', on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton('Enviar', on_click=enviar_mensagem)

    linha_enviar = ft.Row([campo_enviar_mensagem, botao_enviar])
    # deixa o campo e o botão em linha. Poderia ser em Colums pra coluna

    chat = ft.Column()
    # chat precisa ser em coluna, para que apareca um embaixo do outro

    def entrar_chat(evento):
        # fechar popup
        popup.open = False
        # sumir com titulo
        pagina.remove(titulo)
        # sumir com o botao iniciar chat
        pagina.remove(botao)
        # carregar chat
        pagina.add(chat)
        # carregar campo de enviar msg  (juntou ela e a de baixo em uma linha)
        # carregar o botao enviar
        pagina.add(linha_enviar)

        # add no chat a msg "xxx entrou no chat"
        nome_usuario = caixa_nome.value
        mensagem = f'{nome_usuario} entrou no chat'
        pagina.pubsub.send_all(mensagem)
        pagina.update()
        # como está fazendo alteração visual, no fim do código add update

    # criar o popup/modal/alerta
    titulo_popup = ft.Text('Bem vindo ao Zapperson')
    caixa_nome = ft.TextField(label='Digite seu nome', on_submit=entrar_chat)
    botao_popup = ft.ElevatedButton('Entrar no chat', on_click=entrar_chat)
    popup = ft.AlertDialog(
        title=titulo_popup, content=caixa_nome, actions=[botao_popup])
    # actions é pq pode ter mais de um botao. mesmo que seja 1, precisa passar em lista
    # --- tudo isso, adiciona dentro do DEF
    # em caixa_nome add label. se não add ele fica um texto fixo. O label faz com que ele vira uma orientação pro user

    # botão inicial
    botao = ft.ElevatedButton('Iniciar chat', on_click=abrir_popup)
    pagina.add(botao)
    # ----- dentro do ('')  add uma virgula, e aparecerão todas as opções pra editar o botão
    # ----- além disso, define dentro dele o que fará. se for abrir algo novo ou alguma resposta no click,
    # !!! precisa criar o que tem que fazer ANTES da linha do botão
    # o 'botao' é o último item do cdigo aqui, tudo nele vai antes
    # quando o usuário clica, o sistema captura inf's que aconteceram na tela


# executa função
ft.app(main, view=ft.WEB_BROWSER)
# add VIRGULA e view= para mudar a forma que vc verá ele
# por padrão é AppViewer
# pra site/navegador:  , view=ft.WEB_BROWSER


# se quiser disponibilizar isso em rede, precisa fazer o deploy
# só pesquisar flet deploy
# ou fica em servidor gratuito com limites OU servidor pago
