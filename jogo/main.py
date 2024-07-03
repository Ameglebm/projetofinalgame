import pygame
import random

pygame.init()
pygame.font.init()

lista = ["Lucas", "Mariana", "Gabriel", "Sofia", "Arthur", "Isabella", "Matheus", "Ana",
    "Rafael", "Júlia", "Pedro", "Beatriz", "Guilherme", "Laura", "Felipe", "Vitória",
    "Bruno", "Luísa", "Thiago", "Clara", "Rodrigo", "Camila", "Daniel", "Fernanda",
    "Diego", "Larissa", "André", "Manuela", "Marcelo", "Letícia"]

def sortear_nome():
    return random.choice(lista)

sorte = sortear_nome()
cor_texto = (255, 255, 255)
tela = pygame.display.set_mode((900, 700))
pygame.display.set_caption("Sorteio da sorte!")
fonte = pygame.font.Font(None, 76)
texto = fonte.render(sorte, True, cor_texto)

gameloop = True
while gameloop:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            gameloop = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            sorte = sortear_nome()
            texto = fonte.render(sorte, True, cor_texto)
    tela.fill("purple")
    posicao_texto = texto.get_rect(center=(900 //2, 700 //2))
    tela.blit(texto, posicao_texto)
    pygame.display.flip()

pygame.quit()