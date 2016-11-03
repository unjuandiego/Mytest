import pygame


ROJO=(255,0,0)
AZUL=(0,0,255)
VERDE=(0,255,0)
BLANCO=(255,255,255)
NEGRO=(0,0,0)

class Cuadro(pygame.sprite.Sprite):
    def __init__(self, alto, ancho, color):
        pygame.sprite.Sprite.__init__(self)
        self.alto=alto
        self.ancho=ancho
        self.image=pygame.Surface([self.ancho,self.alto])
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.rect.x=0
        self.rect.y=0
