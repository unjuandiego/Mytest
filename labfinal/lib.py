import pygame


ROJO=(255,0,0)
AZUL=(0,0,255)
VERDE=(0,255,0)
BLANCO=(255,255,255)
NEGRO=(0,0,0)

class Jugador2(pygame.sprite.Sprite):
        ls_muros = None
        ls_enem = None
        ls_muere= None
        ls_puerta= None
        ls_tesoro = None
        vel = 2
        choca = 0
        abrir = 0
        vida = 100
        n=0

        def __init__(self, x , y):
            pygame.sprite.Sprite.__init__(self)
            im_player=Recortar('jugador.png',28,28)
            self.image = im_player[0][0]
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.cambiox = 0
            self.cambioy = 0
            self.con=0
            self.dir=2
            self.vel=2


        def update(self):
            self.rect.x += self.cambiox
            ls_golpes = pygame.sprite.spritecollide(self, self.ls_muros, False)
            for m in ls_golpes:
                if self.cambiox > 0:
                    self.rect.right = m.rect.left
                else:
                    self.rect.left = m.rect.right

            self.rect.y += self.cambioy
            ls_golpes = pygame.sprite.spritecollide(self, self.ls_muros, False)
            for m in ls_golpes:
                if self.cambioy > 0:
                    self.rect.bottom = m.rect.top
                else:
                    self.rect.top = m.rect.bottom

            #---------------------------------CHOCA ENEMIGO-----------------------
            ls_choca = pygame.sprite.spritecollide(self, self.ls_enem, False)
            for ch in ls_choca:
                if(self.vida >= 0 ):
                    self.vida -= 0.8
                    pygame.draw.rect(pantalla, NEGRO, [1030, 250, 1140, 300])
                    pantalla.blit(mensaje(str(self.vida),50),[1050,300])
                    pygame.display.flip()
                else:
                    pygame.draw.rect(pantalla, NEGRO, [1030, 250, 1140, 300])
                    self.choca = 1


            ls_chocamu = pygame.sprite.spritecollide(self,self.ls_muere, False)
            for ch in ls_chocamu:
              self.choca = 1

            ls_chocapu = pygame.sprite.spritecollide(self,self.ls_puerta, True)
            for ch in ls_chocapu:
                if self.n == 4:
                     self.abrir = 2



            ls_choj = pygame.sprite.spritecollide(self,self.ls_tesoro, True)
            for ch in ls_choj:
                self.n+=1


        def direccion(self,pos):
            im_player=Recortar('jugador.png',28,28)
            if pos == 1:
                self.image = im_player[0][3]
                self.cambioy = -4
                self.cambiox = 0
            if pos == 2:
                self.image = im_player[0][0]
                self.cambioy = 4
                self.cambiox = 0
            if pos == 3:
                self.image = im_player[0][1]
                self.cambiox = -4
                self.cambioy = 0
            if pos == 4:
                self.image = im_player[0][2]
                self.cambiox = 4
                self.cambioy= 0

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
