import pygame
import sys
import estilos
import random

pygame.init()

largura = 700
altura = 500

#criando a janela
tela = pygame.display.set_mode((largura, altura))

#nome da janela
pygame.display.set_caption("Shape Match") #janela

fonte = pygame.font.SysFont("Arial", 38)
fonte_texto = pygame.font.SysFont("Arial", 18)

botao_jogar = pygame.Rect(250, 250, 200, 45)
botao_sair = pygame.Rect(250, 310, 200, 45)

tela_atual = "menu"

formas = ["circulo", "quadrado", "triangulo", "losango"]

sequencia = random.choices(formas, k=3) #pedindo p escolher os itens de forma aleatoria
print(sequencia)

tempo_inicio = 0
tempo_feedback = 0

rodada = 1
pontos = 0
vidas = 3
posicao = 0

botao_circulo = pygame.Rect(215, 195, 70, 70)
botao_quadrado = pygame.Rect(415, 195, 70, 70)
botao_triangulo = pygame.Rect(215, 320, 70, 70)
botao_losango = pygame.Rect(415, 320, 70, 70)

while True:

    # verifica os eventos
    for evento in pygame.event.get():

        #quita
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #verifica clique do mouse
        if evento.type == pygame.MOUSEBUTTONDOWN:

            #verifica se está no menu
            if tela_atual == "menu":

                #verifica se clicou no botão
                if botao_jogar.collidepoint(evento.pos):
                    tela_atual = "jogo"
                    tempo_inicio = pygame.time.get_ticks()

                if botao_sair.collidepoint(evento.pos):
                    pygame.quit()
                    sys.exit()

            elif tela_atual == "jogador":

                clicado = ""

                if botao_circulo.collidepoint(evento.pos):
                    clicado = "circulo"

                elif botao_quadrado.collidepoint(evento.pos):
                    clicado = "quadrado"

                elif botao_triangulo.collidepoint(evento.pos):
                    clicado = "triangulo"

                elif botao_losango.collidepoint(evento.pos):
                    clicado = "losango"

                if clicado != "":

                    if clicado == sequencia[posicao]:
                        posicao = posicao + 1

                        if posicao == len(sequencia): #ve se acertou a sequencia
                            pontos = pontos + 100
                            rodada = rodada + 1
                            posicao = 0
                            tela_atual = "acertou"
                            tempo_feedback = pygame.time.get_ticks()

                    else:
                        vidas = vidas - 1
                        posicao = 0

                        if vidas == 0:
                            tela_atual = "gameover"

                        else:
                            tela_atual = "errou"
                            tempo_feedback = pygame.time.get_ticks()

    # chamando cor de fundo
    tela.fill(estilos.FUNDO)

    if tela_atual == "menu":

        #texto
        titulo = fonte.render(
            "SHAPE MATCH",
            True,
            estilos.AZUL
        )

        #mostrando o titulo na tela
        tela.blit(titulo, (230, 130))

        #criando a descrição
        texto = fonte_texto.render(
            "Memorize a sequência de formas e repita clicando.",
            True,
            estilos.BRANCO
        )

        #mostrando a descrição
        tela.blit(texto, (150, 190))

        #desenhando o botão
        pygame.draw.rect(tela, estilos.BOTAO, botao_jogar)

        #texto do botão
        texto_jogar = fonte_texto.render(
            "JOGAR",
            True,
            estilos.PRETO
        )

        tela.blit(texto_jogar, (320, 263))

        pygame.draw.rect(tela, estilos.BOTAO, botao_sair)

        texto_sair = fonte_texto.render(
            "SAIR",
            True,
            estilos.PRETO
        )

        tela.blit(texto_sair, (327, 323))

    elif tela_atual == "jogo": #se for jogo, mostra o texto e as formas

        informacoes = fonte_texto.render(
            f"Rodada: {rodada}   Pontos: {pontos}   Vidas: {'<3' * vidas}",
            True,
            estilos.BRANCO
        )

        tela.blit(informacoes, (20, 20))

        texto_jogo = fonte.render(
            "MEMORIZE A SEQUÊNCIA",
            True,
            estilos.AZUL
        )

        tela.blit(texto_jogo, (130, 100))

        quantidade = len(sequencia)
        x = 350 - ((quantidade - 1) * 45)

#definindo proporções
        for forma in sequencia:

            if forma == "circulo":
                pygame.draw.circle(
                    tela,
                    estilos.CIANO,
                    (x, 250),
                    25
                )

            elif forma == "quadrado":
                pygame.draw.rect(
                    tela,
                    estilos.AMARELO,
                    (x - 25, 225, 50, 50)
                )

            elif forma == "triangulo":
                pygame.draw.polygon(
                    tela,
                    estilos.VERDE,
                    [
                        (x, 225),
                        (x - 25, 275),
                        (x + 25, 275)
                    ]
                )

            elif forma == "losango":
                pygame.draw.polygon(
                    tela,
                    estilos.ROXO,
                    [
                        (x, 225),
                        (x + 25, 250),
                        (x, 275),
                        (x - 25, 250)
                    ]
                )

            x = x + 90 #movendo forma

        if pygame.time.get_ticks() - tempo_inicio >= 2000:
            tela_atual = "jogador"

    elif tela_atual == "jogador":

        informacoes = fonte_texto.render(
            f"Rodada: {rodada}   Pontos: {pontos}   Vidas: {'<3' * vidas}",
            True,
            estilos.BRANCO
        )

        tela.blit(informacoes, (20, 20))

        texto_jogador = fonte.render(
            "SUA VEZ!",
            True,
            estilos.AZUL
        )

        tela.blit(texto_jogador, (270, 100))

        progresso = fonte_texto.render(
            f"{posicao + 1} de {len(sequencia)}",
            True,
            estilos.BRANCO
        )

        tela.blit(progresso, (325, 150))

        pygame.draw.circle(
            tela,
            estilos.CIANO,
            (250, 230),
            35
        )

        pygame.draw.rect(
            tela,
            estilos.AMARELO,
            (415, 195, 70, 70)
        )

        pygame.draw.polygon(
            tela,
            estilos.VERDE,
            [
                (250, 320),
                (215, 390),
                (285, 390)
            ]
        )

        pygame.draw.polygon(
            tela,
            estilos.ROXO,
            [
                (450, 320),
                (485, 355),
                (450, 390),
                (415, 355)
            ]
        )

    elif tela_atual == "acertou":

        informacoes = fonte_texto.render(
            f"Rodada: {rodada}   Pontos: {pontos}   Vidas: {'<3' * vidas}",
            True,
            estilos.BRANCO
        )

        tela.blit(informacoes, (20, 20))

        texto_acertou = fonte.render(
            "CORRETO!",
            True,
            estilos.VERDE
        )

        tela.blit(texto_acertou, (260, 220))

        if pygame.time.get_ticks() - tempo_feedback >= 1000:
            sequencia = random.choices(formas, k=rodada + 2)
            print(sequencia)
            tela_atual = "jogo"
            tempo_inicio = pygame.time.get_ticks()

    elif tela_atual == "errou":

        informacoes = fonte_texto.render(
            f"Rodada: {rodada}   Pontos: {pontos}   Vidas: {'♥' * vidas}",
            True,
            estilos.BRANCO
        )

        tela.blit(informacoes, (20, 20))

        texto_errou = fonte.render(
            "ERROU!",
            True,
            estilos.VERMELHO
        )

        tela.blit(texto_errou, (280, 220))

        if pygame.time.get_ticks() - tempo_feedback >= 1000:
            sequencia = random.choices(formas, k=rodada + 2)
            print(sequencia)
            tela_atual = "jogo"
            tempo_inicio = pygame.time.get_ticks()

    elif tela_atual == "gameover":

        texto_gameover = fonte.render(
            "GAME OVER",
            True,
            estilos.VERMELHO
        )

        tela.blit(texto_gameover, (240, 180))

        texto_pontos = fonte_texto.render(
            f"Pontuação: {pontos}",
            True,
            estilos.BRANCO
        )

        tela.blit(texto_pontos, (290, 250))

    #atualizar td
    pygame.display.update()