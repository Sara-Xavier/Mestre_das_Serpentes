import pygame # Biblioteca padrão de games
import random # Usado posteriormente para deixar o lugar da comida da cobra aleatório

pygame.init()

######## Cores ########################
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (213, 50, 80)
verde = (0, 255, 0)
roxo = (82, 86, 204)
######## Cores ########################

######## Configurações da tela ########################
largura = 600
altura = 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Mestre das Serpentes')
######## Configurações da tela ########################

######## Fontes ########################
fonte = pygame.font.SysFont('inter', 35)
clock = pygame.time.Clock()  # Taxa de frames
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
        melhor_score_texto = fonte.render(f'Melhor Score: {melhor_score}', True, verde)
        iniciar_jogo_texto = fonte.render('Pressione Enter Para Iniciar', True, roxo)

        tela.blit(titulo, [largura // 4, altura // 6])
        tela.blit(melhor_score_texto, [largura // 4, altura // 3])
        tela.blit(iniciar_jogo_texto, [largura // 6, altura // 2])
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # ENTER PARA INICIAR
                    menu_ativo = False

# Função principal do jogo
def jogo():
    global melhor_score
    fim_jogo = False
    sair_jogo = False

    x_cobra = largura // 2
    y_cobra = altura // 2
    x_cobra_mudanca = 0
    y_cobra_mudanca = 0
    lista_cobra = []
    comprimento_cobra = 1
    score = 0

    comida_x = round(random.randrange(0, largura - 10) / 10.0) * 10.0
    comida_y = round(random.randrange(0, altura - 10) / 10.0) * 10.0

    while not sair_jogo:
        while fim_jogo:
            tela.fill(preto)
            
            # Mensagens divididas em duas linhas
            mensagem_fim_1 = fonte.render("Fim de jogo!", True, vermelho)
            mensagem_fim_2 = fonte.render("Pressione C para continuar ou Q para sair", True, vermelho)
            
            # Exibe cada linha em uma posição diferente
            tela.blit(mensagem_fim_1, [largura // 4, altura // 3])
            tela.blit(mensagem_fim_2, [largura // 10, altura // 2])
            
            pygame.display.update()


            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sair_jogo = True
                        fim_jogo = False
                    if event.key == pygame.K_c:
                        if score > melhor_score:
                            melhor_score = score
                        jogo()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair_jogo = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_cobra_mudanca = -10
                    y_cobra_mudanca = 0
                elif event.key == pygame.K_RIGHT:
                    x_cobra_mudanca = 10
                    y_cobra_mudanca = 0
                elif event.key == pygame.K_UP:
                    y_cobra_mudanca = -10
                    x_cobra_mudanca = 0
                elif event.key == pygame.K_DOWN:
                    y_cobra_mudanca = 10
                    x_cobra_mudanca = 0

        x_cobra += x_cobra_mudanca
        y_cobra += y_cobra_mudanca

        if x_cobra >= largura or x_cobra < 0 or y_cobra >= altura or y_cobra < 0:
            fim_jogo = True

        tela.fill(preto)
        pygame.draw.rect(tela, verde, [comida_x, comida_y, 10, 10])

        cabeca_cobra = []
        cabeca_cobra.append(x_cobra)
        cabeca_cobra.append(y_cobra)
        lista_cobra.append(cabeca_cobra)

        if len(lista_cobra) > comprimento_cobra:
            del lista_cobra[0]

        for bloco in lista_cobra[:-1]:
            if bloco == cabeca_cobra:
                fim_jogo = True

        for bloco in lista_cobra:
            pygame.draw.rect(tela, branco, [bloco[0], bloco[1], 10, 10])

        pygame.display.update()

        if x_cobra == comida_x and y_cobra == comida_y:
            comida_x = round(random.randrange(0, largura - 10) / 10.0) * 10.0
            comida_y = round(random.randrange(0, altura - 10) / 10.0) * 10.0
            comprimento_cobra += 1
            score += 1

        clock.tick(15)

    pygame.quit()
    quit()

# Executando o jogo
exibir_menu()
jogo()
