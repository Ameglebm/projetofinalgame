import pygame
import random

pygame.init()
pygame.font.init()

lista = ["amar", "azul", "acordado", "amargura", "assistir", "apetecer", "ascender", "arrojado", 
    "aprender", "alcançar", "atribuir", "anarquia", "amistoso", "arretado", "ajudante", 
    "atraente"]

contador = 0

def sortear_nome():
    return random.choice(lista).upper()

sorte = sortear_nome()
letras_acertadas = []
letras_erradas = []

cor_texto = (255, 255, 255)
cor_fundo = (75, 0, 130)

tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Jogo da Forca!")
fonte = pygame.font.Font(None, 58)
fonte_pequena = pygame.font.Font(None, 34)
fonte_media = pygame.font.Font(None, 52)

def desenhar_forca(tela, erros):
    # Desenhando a estrutura da forca
    base_x, base_y = 20, 500
    pygame.draw.line(tela, cor_texto, (base_x, base_y), (base_x + 200, base_y), 6)
    pygame.draw.line(tela, cor_texto, (base_x + 100, base_y), (base_x + 100, base_y - 400), 10)
    pygame.draw.line(tela, cor_texto, (base_x + 100, base_y - 400), (base_x + 250, base_y - 400), 10)
    pygame.draw.line(tela, cor_texto, (base_x + 250, base_y - 400), (base_x + 250, base_y - 350), 10)

    if erros > 0:
        pygame.draw.circle(tela, cor_texto, (base_x + 250, base_y - 320), 30, 10) # Cabeça
    if erros > 1:
        pygame.draw.line(tela, cor_texto, (base_x + 250, base_y - 290), (base_x + 250, base_y - 200), 10) # Tronco
    if erros > 2:
        pygame.draw.line(tela, cor_texto, (base_x + 250, base_y - 250), (base_x + 200, base_y - 300), 10) # Braço esquerdo
    if erros > 3:
        pygame.draw.line(tela, cor_texto, (base_x + 250, base_y - 250), (base_x + 300, base_y - 300), 10) # Braço direito
    if erros > 4:
        pygame.draw.line(tela, cor_texto, (base_x + 250, base_y - 200), (base_x + 200, base_y - 150), 10) # Perna esquerda
    if erros > 5:
        pygame.draw.line(tela, cor_texto, (base_x + 250, base_y - 200), (base_x + 300, base_y - 150), 10) # Perna direita

def mostrar_palavra(tela, palavra, letras_acertadas):
    exibicao = ""
    for letra in palavra:
        if letra in letras_acertadas:
            exibicao += letra + " "
        else:
            exibicao += "_ "
    texto = fonte.render(exibicao, True, cor_texto)
    tela.blit(texto, (500 - texto.get_width() // 2, 467))  # Abaixo da força

def mostrar_letras_erradas(tela, letras_erradas):
    texto = fonte_pequena.render("Erros: " + ", ".join(letras_erradas), True, cor_texto)
    tela.blit(texto, (10, 10))

def desenhar_botao(tela, texto, pos, tamanho):
    botao = pygame.Rect(pos, tamanho)
    pygame.draw.rect(tela, cor_texto, botao, border_radius=20)
    texto_render = fonte_pequena.render(texto, True, cor_fundo)
    tela.blit(texto_render, (pos[0] + (tamanho[0] - texto_render.get_width()) // 2, pos[1] + (tamanho[1] - texto_render.get_height()) // 2))
    return botao

estado_jogo = "menu"

def resetar_jogo():
    global sorte, letras_acertadas, letras_erradas, estado_jogo
    sorte = sortear_nome()
    letras_acertadas = []
    letras_erradas = []
    estado_jogo = "jogando"

gameloop = True
while gameloop:
    tela.fill(cor_fundo)
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            gameloop = False

        elif evento.type == pygame.KEYDOWN:
            if estado_jogo == "jogando":
                letra = evento.unicode.upper()

                if letra.isalpha() and len(letra) == 1:
                    if letra in sorte and letra not in letras_acertadas:
                        letras_acertadas.append(letra)
                    elif letra not in sorte and letra not in letras_erradas:
                        letras_erradas.append(letra)

        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if estado_jogo == "menu":

                if botao_play.collidepoint(evento.pos):
                    resetar_jogo()

            elif estado_jogo == "venceu":
                if botao_continuar.collidepoint(evento.pos):
                    contador += 1

                    resetar_jogo()
            elif estado_jogo == "perdeu":
                if botao_tentar_novamente.collidepoint(evento.pos):
                    contador = 0
                    resetar_jogo()

    if estado_jogo == "menu":
        botao_play = desenhar_botao(tela, "Play", (350, 250), (100, 50))

    elif estado_jogo == "jogando":
        mostrar_palavra(tela, sorte, letras_acertadas)
        mostrar_letras_erradas(tela, letras_erradas)
        desenhar_forca(tela, len(letras_erradas))

        if set(sorte) <= set(letras_acertadas):
            estado_jogo = "venceu"

        elif len(letras_erradas) >= 6:
            estado_jogo = "perdeu"
    elif estado_jogo == "venceu":
        
        texto_vitoria = fonte_media.render("Você Venceu!", True, cor_texto)
        tela.blit(texto_vitoria, (400 - texto_vitoria.get_width() // 2, 250))

        botao_continuar = desenhar_botao(tela, "Continuar", (350, 400), (100, 50))

        texto_pontos = fonte_pequena.render(f"Pontos: {contador}", True, cor_texto)

        tela.blit(texto_pontos, (350, 350))
    elif estado_jogo == "perdeu":
        texto_derrota = fonte_pequena.render(f"Você Perdeu! Era: {sorte}", True, cor_texto)
        tela.blit(texto_derrota, (400 - texto_derrota.get_width() // 2, 250))

        botao_tentar_novamente = desenhar_botao(tela, "Tentar Novamente", (300, 400), (200, 50))

        texto_pontos = fonte_pequena.render(f"Pontos: {contador}", True, cor_texto)
        tela.blit(texto_pontos, (350, 350))
    
    pygame.display.flip()

pygame.quit()
