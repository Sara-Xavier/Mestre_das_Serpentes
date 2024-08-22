import pygame # Biblioteca padrão de games
import random # Usado posteriormente para deixar o lugar da comida da cobra aleatório

pygame.init()

######## Cores ########################
branco = (255, 255, 255)
preto = (0, 0, 0,)
vermelho = (213, 50, 80)
verde = (0, 255, 0)
roxo = (82,86,204)
######## Cores ########################

######## Confugurações da tela ########################
largura = 600
altura = 400
tela = pygame.display.set_caption('Mestre das Serpentes')
######## Confugurações da tela ########################

######## Fontes ########################
fonte = pygame.font.SysFont('inter', 35)
clock = pygame.time.Clock()  #Taxa de frames
######## Fontes ########################

######## Melhor Score ########################
melhor_score = 0
######## Melhor Score ########################


######## Exibição/Configurações de Menu ########################
def exibir_menu():
    menu_ativo = True
    while menu_ativo:
        tela.fill(preto)
        titulo = fonte.render('Mestre das Serpentes', True, branco)
        melhor_score_texto = fonte.render(f'Melhor Score: {melhor_score}, True, verde')
        iniciar_jogo_texto = fonte.render('Pressione Enter Para Iniciar', True, roxo)
######## Exibição/Configurações de Menu ########################