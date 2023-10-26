import customtkinter
from PIL import Image, ImageTk
import pygame
import pandas as pd
import sqlite3
from codigo import *

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

janela_dois = customtkinter.CTk()
janela_dois.geometry('1000x600')
janela_dois.title('Museu do Botafogo')

janela_dois.iconbitmap('download.ico')

#Função história do clube
def historia():

    janela_tres = customtkinter.CTkToplevel(janela_dois)
    janela_tres.geometry('1500x720')
    janela_tres.title("História")
    janela_tres.attributes('-topmost', True)
    texto_historia = customtkinter.CTkLabel(janela_tres, text='''No ano de 1904, surgia no bairro de Botafogo um novo clube de futebol, o Electro Club, primeiro nome dado ao Botafogo Football Club. 
    A associação nasceu de uma conversa entre dois amigos durante uma aula. 
    Flávio Ramos e Emmanuel Sodré estudavam no colégio Alfredo Gomes e, durante uma aula de álgebra, nascia a primeira ideia de fundar um clube, através 
    de um bilhete passado por Flávio a Emmanuel, que dizia: "O Ithamar tem um clube de football na Rua Martins Ferreira. 
    Vamos fundar outro no Largo dos Leões? Podemos falar aos Werneck, ao Arthur César, ao Vicente e ao Jacques". 
    E assim tudo começou.
    Esse bilhete foi interceptado pelo professor de matemática, general Júlio Noronha, que advertiu não ser aquele o momento mais apropriado para conversas daquele tipo, 
    ressaltando, porém, que apoiava qualquer ideia relativa à prática de esportes. 
    Estava dado então o primeiro passo para o nascimento do Glorioso".''', font=customtkinter.CTkFont(family='Arial Black',
    size=14))

    texto_historia.pack(padx=10, pady=10)
    image1 = Image.open('jogadores_fundadores_1904.jpg')
    test = ImageTk.PhotoImage(image1)
    label1 = customtkinter.CTkLabel(janela_tres, image=test, text='')
    label1.pack(padx=10, pady=10)


def idolos():
    
    janela_quatro = customtkinter.CTkToplevel(janela_dois)
    janela_quatro.geometry('1500x720')
    janela_quatro.title('Ídolos do Botafogo')
    janela_quatro.attributes('-topmost', True)
    texto_idolos = customtkinter.CTkLabel(janela_quatro, text=''' Mané Garrincha: Driblador mágico, encantou o mundo com sua habilidade única.

Nilton Santos: Conhecido como "A Enciclopédia", foi um dos melhores laterais da história, tanto no Botafogo quanto na seleção.

Jairzinho: Apelidado de "Furacão da Copa", foi peça crucial na conquista da Copa de 1970.

Zagallo: Jogador talentoso e lendário técnico, deixou um legado inestimável.

Amarildo: Atacante goleador, contribuiu para vitórias memoráveis do Botafogo.

Didi: Meio-campista criativo, famoso por sua visão de jogo excepcional.

Paulo Cézar: Ponta-direita habilidoso, conhecido por dribles e cruzamentos precisos.

Gerson: Apelidado de "Canhotinha de Ouro", suas habilidades de passe eram extraordinárias.

Carlos Alberto Torres: Capitão do Brasil em 1970, era um lateral excepcional.

Túlio Maravilha: Terceiro maior artilheiro do clube, famoso por seus gols.
''', font= customtkinter.CTkFont(family='Arial Black',
size=12))
    texto_idolos.pack(padx=10, pady=10)
    image2 = Image.open('mural-idolos-botafogo-fogo-hebreu-fogaonet_resized_resized.jpg')
    test = ImageTk.PhotoImage(image2)
    label2 = customtkinter.CTkLabel(janela_quatro, image=test, text='')
    label2.pack(padx=10, pady=1)

def tocar_hino():
    pygame.mixer.init()
    pygame.mixer.music.load('hino-do-botafogo.mp3')
    pygame.mixer.music.play()

def parar_hino():
    pygame.mixer.music.stop()

def hino():
    janela_cinco = customtkinter.CTkToplevel(janela_dois)
    janela_cinco.geometry('1000x720')
    janela_cinco.title('Hino do Botafogo')
    janela_cinco.attributes('-topmost', True)
    texto_hino = customtkinter.CTkLabel(janela_cinco, text='''Botafogo, Botafogo, campeão desde 1910
Foste herói em cada jogo, Botafogo
Por isso é que tu és e hás de ser nosso imenso prazer
Tradições aos milhões tens também
Tu és o glorioso não podes perder, perder para ninguém!
Noutros esportes tua fibra está presente
Honrando as cores do Brasil de nossa gente
Na estrada dos louros, um facho de luz
Tua estrela solitária te conduz
Botafogo, Botafogo, campeão desde 1910
Foste herói em cada jogo, Botafogo
Por isso é que tu és e hás de ser nosso imenso prazer
Tradições aos milhões tens também
Tu és o glorioso, não podes perder, perder para ninguém!
Noutros esportes tua fibra está presente
Honrando as cores do Brasil de nossa gente
Na estrada dos louros, um facho de luz
Tua estrela solitária te conduz''', font=customtkinter.CTkFont(family='Arial Black',
size=18))
    texto_hino.pack()

    botao_tocar_hino = customtkinter.CTkButton(janela_cinco, text='Tocar Hino',
                                               font=customtkinter.CTkFont(family='Arial Black',size=20),
                                               height=20, width=20, command=tocar_hino)
    botao_tocar_hino.pack()

    botao_parar_hino = customtkinter.CTkButton(janela_cinco, text='Parar Hino',
                                               font=customtkinter.CTkFont(family='Arial Black', size=20),
                                               height=20, width=20, command=parar_hino)    
    botao_parar_hino.pack(padx=10, pady=10)

def virar_membro():
    janela = customtkinter.CTkToplevel(janela_dois)
    janela.geometry('1000x600')

    conexao = sqlite3.connect('usuarios_cadastrados.db')
    c = conexao.cursor()
    c.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='usuarios' ''')
    if c.fetchone()[0] == 0:
        c.execute('''CREATE TABLE usuarios(
            nome TEXT,
            idade INTEGER,
            email TEXT,
            cpf INTEGER)''')
    conexao.commit()
    conexao.close()

    def login():
        conexao = sqlite3.connect('usuarios_cadastrados.db')

        c = conexao.cursor()

        c.execute(' INSERT INTO usuarios VALUES (:nome, :idade, :email, :cpf)',
                  {
                      'nome': nome_login.get(),
                      'idade': idade_login.get(),
                    'email': email_login.get(),
                    'cpf': cpf_login.get()
                }
                )

        conexao.commit()

        conexao.close()

        nome_login.delete(0, 'end')
        idade_login.delete(0, 'end')
        email_login.delete(0, 'end')
        cpf_login.delete(0, 'end')

        nome = str(nome_login.get())
        idade = str(idade_login.get())
        email = str(email_login.get())
        cpf = str(cpf_login.get())
        login_init = Login(nome, idade, email, cpf)

    def exportar_usuario():
        conexao = sqlite3.connect('usuarios_cadastrados.db')

        c = conexao.cursor()

        c.execute('SELECT *, oid FROM usuarios')
        clientes_cadastrados = c.fetchall()
        clientes_cadastrados = pd.DataFrame(clientes_cadastrados, columns=['nome', 'idade', 'email', 'cpf', 'id'])
        clientes_cadastrados.to_csv('banco_de_clientes')

        conexao.commit()

        conexao.close()

    texto_principal = customtkinter.CTkLabel(janela, text='Cadastro de Membro',
                                         font=customtkinter.CTkFont(family='Arial Black', size=30), text_color='white')
    texto_principal.pack(padx=10, pady=20)

    nome_login = customtkinter.CTkEntry(janela, placeholder_text='Seu nome', placeholder_text_color='white',
                                    font=customtkinter.CTkFont(family='Arial Black', size=13))
    nome_login.pack(padx=10, pady=10)

    idade_login = customtkinter.CTkEntry(janela, placeholder_text='Sua idade', placeholder_text_color='white',
                                     font=customtkinter.CTkFont(family='Arial Black', size=13))
    idade_login.pack(padx=10, pady=10)

    email_login = customtkinter.CTkEntry(janela, placeholder_text='Seu e-mail', placeholder_text_color='white',
                                     font=customtkinter.CTkFont(family='Arial Black', size=13))
    email_login.pack(padx=10, pady=10)

    cpf_login = customtkinter.CTkEntry(janela, placeholder_text='Seu CPF', placeholder_text_color='white',
                                   font=customtkinter.CTkFont(family='Arial Black', size=13))
    cpf_login.pack(padx=10, pady=10)

    botao_login = customtkinter.CTkButton(janela, text='Cadastrar Usuário',
                                      font=customtkinter.CTkFont(family='Arial Black', size=20)
                                      , height=20, width=20, command=login)
    botao_login.pack(padx=10, pady=10)

    botao_exportar_usuario = customtkinter.CTkButton(janela, text='Exportar usuários',
                                                 font=customtkinter.CTkFont(family='Arial Black', size=20)
                                                 , height=20, width=20, command=exportar_usuario)
    botao_exportar_usuario.pack(padx=10, pady=10)

#TELAS E BOTÕES
texto_tela_principal = customtkinter.CTkLabel(janela_dois, text='Museu do Botafogo',
                                              font=customtkinter.CTkFont(family='Arial Black', size=30),
                                              text_color='white')
texto_tela_principal.pack(padx=10, pady=10)

botao_historia = customtkinter.CTkButton(janela_dois, text='História',
                                         font=customtkinter.CTkFont(family='Arial Black', size=20),
                                         height=20, width=20, command=historia)
botao_historia.pack(padx=35, pady=35)

botao_idolos = customtkinter.CTkButton(janela_dois, text='Idolos',
                                       font=customtkinter.CTkFont(family='Arial Black', size=20),
                                       height=20, width=20, command=idolos)
botao_idolos.pack(padx=35, pady=35)

botao_hino = customtkinter.CTkButton(janela_dois, text='Hino',
                                     font=customtkinter.CTkFont(family='Arial Black', size=20),
                                     height=20, width=20, command=hino)
botao_hino.pack(padx=35, pady=35)

botao_virar_membro = customtkinter.CTkButton(janela_dois, text='Virar membro',
                                             font=customtkinter.CTkFont(family='Arial Black', size=20),
                                             height=20, width=20, command=virar_membro)
botao_virar_membro.pack(padx=35, pady=35)

janela_dois.mainloop()