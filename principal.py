import pygame
# Não importei  from pygame.locals import*
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
        self.todas_as_sprites = pygame.sprite.Group()
        self.rodar()

    def rodar(self):
        #Loop do jogo
        self.jogando = True
        while self.jogando:
            # TAXA FRAMES DO JOGO
            self.relogio.tick(constantes.FPS)
            self.eventos()
            self.atualizar_sprites()
            self.desenhar_sprites()
        
    def eventos(self):
        #Define os eventos do jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.jogandO:
                    self.jogando: False
                self.esta_jogando = False

    def  atualizar_sprites()
        #Atualiza sprites

