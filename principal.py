import pygame
import constantes
import sprites

class Game:
    def __init__(self):
        # Criando uma tela para o jogo
        pygame.init() 
        pygame.mixer.init()  
        self.tela = pygame.display.set_mode((constantes.LARGURA, constantes.ALTURA))
        pygame.display.set_caption(constantes.TITULO_JOGO)
        self.relogio = pygame.time.Clock()
        self.esta_rodando = True
    
    def novo_jogo(self):
        # Instancia as classes das sprites do jogo
        self.todas_as_sprites = 
