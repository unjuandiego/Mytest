import pygame
import ConfigParser
from lib import *
import random
import time
from bresenham import *

ANCHO=1020
ALTO=670

ROJO=(255,0,0)
AZUL=(0,0,255)
VERDE1=(0,255,0)
BLANCO=(255,255,255)
NEGRO=(0,0,0)
VERDE=(67,83,46)

def Recortar(archivo, ancho, alto):
    imagen=pygame.image.load(archivo).convert_alpha()
    img_ancho, img_alto=imagen.get_size()
    tabla_fondos=[]
    for fondo_x in range(0,img_ancho/ancho):
        linea=[]
        tabla_fondos.append(linea)
        for fondo_y in range(0,img_alto/alto):
            cuadro=(fondo_x*ancho, fondo_y*alto, ancho, alto)
            linea.append(imagen.subsurface(cuadro))
    return tabla_fondos
def mensaje(msj,n):
    font=pygame.font.Font(None,n)
    texto=font.render(msj,True,BLANCO)
    return texto

class Enemigo2(pygame.sprite.Sprite):
    ls_muros=None
    movimientos = []
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        im_enemigo=Recortar('enemigo.png',28,28)
        self.image = im_enemigo[9][0]
        self.rect = self.image.get_rect()
        self.vel = 0
        self.t=100
        self.arriba = False
        self.rect.x = x
        self.rect.y = y
        self.cambiox = 0
        self.cambioy = 0
    def update(self):
        x1=0
        y1=0
        self.movimientos = bresenham([self.rect.x,self.rect.y],[Jugador2.ls_mov[0],Jugador2.ls_mov[1]])
        for pos in self.movimientos.path:
        	x1 = pos[0]
        	y1 = pos[1]
        print x1,y1
        self.rect.x = x1
        self.rect.y = y1
            #self.cambiox = x1

        #Esta es por si los enemigos aparecen metidos dentro de los muros
        ls_golpes = pygame.sprite.spritecollide(self, self.ls_muros, False)
        for m in ls_golpes:
            self.rect.right = m.rect.left

class Enemigo(pygame.sprite.Sprite):
    ls_muros=None
    def __init__(self,v,cx,cy):
        pygame.sprite.Sprite.__init__(self)
        im_enemigo=Recortar('enemigo.png',28,28)
        self.image = im_enemigo[9][0]
        self.rect = self.image.get_rect()
        self.vel = v
        self.t=100
        self.arriba = False
        self.rect.x = x
        self.rect.y = y
        self.cambiox = cx
        self.cambioy = cy
    def update(self):
        self.rect.y +=self.cambioy
        if self.rect.y > (ALTO):
            self.cambioy= -self.vel
        elif self.rect.y <= 0:
            self.cambioy = self.vel

        ls_golpes = pygame.sprite.spritecollide(self, self.ls_muros, False)
        for m in ls_golpes:
            if self.cambioy > 0:
                self.rect.bottom = m.rect.top
                self.cambioy = -self.vel

            else:
                self.rect.top = m.rect.bottom
                self.cambioy = self.vel
        #Esta es por si los enemigos aparecen metidos dentro de los muros
        ls_golpes = pygame.sprite.spritecollide(self, self.ls_muros, False)
        for m in ls_golpes:
            self.rect.right = m.rect.left

class LLave(pygame.sprite.Sprite):
    def __init__(self,x,y,archivo):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def update(self):
        pass

class J(pygame.sprite.Sprite):
    def __init__(self,x,y,archivo):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass

class puerta_n2(pygame.sprite.Sprite):
    bloqueo = False
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        im_puerta=Recortar('jungle1.png',32,32)
        self.image = im_puerta[5][5]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass

class tesoro(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        im_puerta=Recortar('jungle1.png',32,32)
        self.image = im_puerta[17][2]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass

class U(pygame.sprite.Sprite):
    def __init__(self,x,y,archivo):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass

class N(pygame.sprite.Sprite):
    def __init__(self,x,y,archivo):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass

class G(pygame.sprite.Sprite):
    def __init__(self,x,y,archivo):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass

class L(pygame.sprite.Sprite):
    def __init__(self,x,y,archivo):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass

class E(pygame.sprite.Sprite):
    def __init__(self,x,y,archivo):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass

class Muro(pygame.sprite.Sprite):
    def __init__(self, x , y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([32,32])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def update(self):
      pass

class Muere(pygame.sprite.Sprite):
    def __init__(self, x , y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([32,32])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def update(self):
      pass

class Puerta(pygame.sprite.Sprite):
    def __init__(self, x , y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([32,32])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def update(self):
      pass

class Nivel:
    def __init__(self, infomapa, G_muros,G_muere, G_puerta):
        self.interprete=ConfigParser.ConfigParser()
        self.interprete.read(infomapa)
        self.origen = self.interprete.get("nivel", "origen")
        self.alto = int (self.interprete.get("nivel", "alto"))
        self.ancho = int (self.interprete.get("nivel", "ancho"))
        self.fondo = self.Recortar(self.origen, self.ancho, self.alto)
        self.mapa = []
        self.mapa = self.interprete.get("nivel", "mapa").split("\n")
        self.muros  = G_muros
        self.muere = G_muere
        self.puerta = G_puerta


    def Recortar(self, archivo, ancho, alto):
        imagen = pygame.image.load(archivo).convert_alpha()
        img_ancho, img_alto = imagen.get_size()
        print img_ancho, ' ', img_alto
        tabla_fondos = []
        for fondo_x in range(0, img_ancho/ancho):
            linea=[]
            tabla_fondos.append(linea)
            for fondo_y in range(0, img_alto/alto):
                cuadro = (fondo_x*ancho, fondo_y*alto, ancho, alto)
                linea.append(imagen.subsurface(cuadro))
        return tabla_fondos

    def Dibujar(self, pantalla):
        var_x = self.ancho
        var_y = self.alto
        con_y = 0
        for fila in self.mapa:
            con_x=0
            for c in fila:
                x = int(self.interprete.get(c, "x"))
                y = int(self.interprete.get(c, "y"))
                cuadro_sel=self.fondo[x][y]
                pantalla.blit(cuadro_sel, [con_x, con_y])
                con_x+=var_x
            con_y+=var_y

    def Muros_ls(self):
        var_x = self.ancho
        var_y = self.alto
        con_y = 0
        ls_muros = None
        for fila in self.mapa:
            con_x=0
            for c in fila:
                if self.interprete.get(c, "muro") == "si":
                    muro = Muro(con_x, con_y)
                    self.muros.add(muro)
                con_x+=var_x
            con_y+=var_y
        return self.muros

    def Muere_ls(self):
        var_x = self.ancho
        var_y = self.alto
        con_y = 0
        ls_muere = None
        for fila in self.mapa:
            con_x=0
            for c in fila:
                if self.interprete.get(c, "muere") == "si":
                    muere = Muere(con_x, con_y)
                    self.muere.add(muere)
                con_x+=var_x
            con_y+=var_y
        return self.muere

    def Puerta_ls(self):
        var_x = self.ancho
        var_y = self.alto
        con_y = 0
        ls_puerta = None
        for fila in self.mapa:
            con_x=0
            for c in fila:
                if self.interprete.get(c, "puerta") == "si":
                    puerta = Puerta(con_x, con_y)
                    self.puerta.add(puerta)
                con_x+=var_x
            con_y+=var_y
        return self.puerta

class Jugador(pygame.sprite.Sprite):
        ls_muros = None
        ls_mod = None
        ls_enem = None
        ls_muere= None
        ls_llaves= None
        ls_puerta= None
        ls_j = None
        ls_u = None
        ls_n = None
        ls_g = None
        ls_l = None
        ls_e = None
        vel = 2
        choca = 0
        vida = 100
        n=0
        llav = False

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

            ls_chocapu = pygame.sprite.spritecollide(self,self.ls_puerta, False)
            if self.llav == True:
             for ch in ls_chocapu:
               self.choca = 2

            ls_chollave = pygame.sprite.spritecollide(self,self.ls_llaves, False)
            for ch in ls_chollave:
                self.llav = True
                for l in self.ls_llaves:
                    l.rect.x, l.rect.y = 1060,100

            ls_choj = pygame.sprite.spritecollide(self,self.ls_j, False)
            for ch in ls_choj:
                self.n+=1
                for l in self.ls_j:
                    l.rect.x, l.rect.y = 1060,400

            ls_chou = pygame.sprite.spritecollide(self,self.ls_u, False)
            for ch in ls_chou:
                self.n+=1
                for l in self.ls_u:
                    l.rect.x, l.rect.y = 1060,440

            ls_chon = pygame.sprite.spritecollide(self,self.ls_n, False)
            for ch in ls_chon:
                self.n+=1
                for l in self.ls_n:
                    l.rect.x, l.rect.y = 1060,480

            ls_chog = pygame.sprite.spritecollide(self,self.ls_g, False )
            for ch in ls_chog:
                self.n+=1
                for l in self.ls_g:
                    l.rect.x, l.rect.y = 1060,520

            ls_chol = pygame.sprite.spritecollide(self,self.ls_l, False)
            for ch in ls_chol:
                self.n+=1
                for l in self.ls_l:
                    l.rect.x, l.rect.y = 1060,560

            ls_choe = pygame.sprite.spritecollide(self,self.ls_e, False )
            for ch in ls_choe:
                self.n+=1
                for l in self.ls_e:
                    l.rect.x, l.rect.y = 1060,600

            if self.n==6:
                self.choca=2


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

class Jugador2(pygame.sprite.Sprite):
        ls_muros = None
        ls_enem = None
        ls_muere= None
        ls_puerta= None
        ls_tesoro = None
        ls_puerta1 = None
        ls_enem2 = None
        ls_mov=[0,0]
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

            ls_chocapu = pygame.sprite.spritecollide(self,self.ls_puerta1, False)
            for ch in ls_chocapu:
                for puertica in self.ls_puerta1:
                    if puertica.bloqueo==False:
                        if self.cambioy > 0:
                           self.rect.bottom = puertica.rect.top
                        else:
                           self.rect.top = puertica.rect.bottom
                    if puertica.bloqueo==True:
                        pygame.sprite.spritecollide(self,self.ls_puerta1, True)

                if self.n == 4:
                     for puertica in self.ls_puerta1:
                         puertica.bloqueo = True




            ls_chots = pygame.sprite.spritecollide(self,self.ls_tesoro, True)
            for ch in ls_chots:
                self.n+=1

            ls_chocapu = pygame.sprite.spritecollide(self,self.ls_puerta, False)
            for ch in ls_chocapu:
                self.choca = 2



        def direccion(self,pos):
            im_player=Recortar('jugador.png',28,28)
            if pos == 1:
                self.image = im_player[0][3]
                self.cambioy = -4
                self.cambiox = 0
                self.ls_mov =[self.rect.x,self.rect.y]
                #print self.ls_mov
                self.ls_mov=[]
                Enemigo2.movimientos = []
            if pos == 2:
                self.image = im_player[0][0]
                self.cambioy = 4
                self.cambiox = 0
                self.ls_mov =[self.rect.x,self.rect.y]
                print self.ls_mov
                self.ls_mov=[]
                Enemigo2.movimientos = []
            if pos == 3:
                self.image = im_player[0][1]
                self.cambiox = -4
                self.cambioy = 0
                self.ls_mov =[self.rect.x,self.rect.y]
                #print self.ls_mov
                self.ls_mov=[]
                Enemigo2.movimientos = []
            if pos == 4:
                self.image = im_player[0][2]
                self.cambiox = 4
                self.cambioy= 0
                self.ls_mov =[self.rect.x,self.rect.y]
                #print self.ls_mov
                self.ls_mov=[]
                Enemigo2.movimientos = []
if __name__ == '__main__':
   pygame.init()
   pantalla=pygame.display.set_mode([ANCHO+125,ALTO])

   pantalla.blit(mensaje("Porcentaje de vida",20),[1023,180])
   pantalla.blit(mensaje("100",50),[1050,300])

   todos=pygame.sprite.Group()
   muere = pygame.sprite.Group()
   muros = pygame.sprite.Group()
   puertas = pygame.sprite.Group()

   nivel1 = Nivel('nivel.map', muros, muere, puertas)
   muros = nivel1.Muros_ls()
   muere = nivel1.Muere_ls()
   puertas = nivel1.Puerta_ls()
   nivel1.Dibujar(pantalla)

   jp=Jugador(32,32)
   todos.add(jp)
   jp.ls_muros = muros

   llave = pygame.sprite.Group()
   ll= LLave(450,38,"llave.png")
   llave.add(ll)
   todos.add(ll)

   jp.ls_llaves = llave

   j = pygame.sprite.Group()
   t = J(230,200,"j.jpg")
   j.add(t)
   todos.add(t)

   jp.ls_j = j

   u = pygame.sprite.Group()
   tu= U(520,455,"u.jpg")
   u.add(tu)
   todos.add(tu)

   jp.ls_u = u

   n = pygame.sprite.Group()
   tul = N(100,38,"n.jpg")
   n.add(tul)
   todos.add(tul)

   jp.ls_n = n

   g = pygame.sprite.Group()
   tulg = G(450,195,"g.jpg")
   g.add(tulg)
   todos.add(tulg)

   jp.ls_g = g

   l = pygame.sprite.Group()
   tulgl = L(965,600,"l.jpg")
   l.add(tulgl)
   todos.add(tulgl)

   jp.ls_l = l

   e = pygame.sprite.Group()
   tulgle= E(775,390,"e.jpg")
   e.add(tulgle)
   todos.add(tulgle)

   jp.ls_e = e

   n=32
   cen=[[3*n,15*n],[3*n,6*n],[6*n,5*n],[15*n,17*n],[4*n,15*n],[13*n,17*n],[10*n,9*n],
        [21*n,8*n],[15*n,2*n],[10*n,17*n],[30*n,15*n],[28*n,14*n],[5*n,9*n],[22*n,18*n],[18*n,11*n],[18*n,18*17],
        [22*n,12*n],[25*n,12*n],[27*n,19*n]]

   enemigos = pygame.sprite.Group()
   for i in range(19):
       x = cen[i][0]
       y = cen[i][1]
       e = Enemigo(1,1,1)
       e.rect.x = x
       e.rect.y = y
       e.vel = 1
       enemigos.add(e)
       todos.add(e)
       e.ls_muros = muros

   jp.ls_enem = enemigos
   jp.ls_muere = muere
   jp.ls_puerta = puertas

   font=pygame.font.Font(None,80)
   texto=font.render("GAME OVER",True,NEGRO)
   gano=font.render("Ganaste",True,NEGRO)
   nivel2=font.render("NIVEL 2",True,BLANCO)
   pygame.display.flip()
   ganar=False
   fin= False
   pausa = False
   while not fin:
      for event in pygame.event.get():
          if event.type== pygame.QUIT:
             fin=True
          if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_UP:

                  jp.direccion(1)
              if event.key == pygame.K_DOWN:

                  jp.direccion(2)

              if event.key == pygame.K_LEFT:
                  jp.direccion(3)

              if event.key == pygame.K_RIGHT:
                  jp.direccion(4)

              if event.key ==pygame.K_f:

                  ganar=True

              if event.key ==pygame.K_p:
                  if pausa:
                    pausa = False
                  else:
                    pausa = True

          if event.type == pygame.KEYUP:
                  if event.key == pygame.K_UP:
                        jp.cambioy = 0
                  if event.key == pygame.K_DOWN:
                        jp.cambioy = 0
                  if event.key == pygame.K_RIGHT:
                        jp.cambiox = 0
                  if event.key == pygame.K_LEFT:
                        jp.cambiox = 0

      if jp.choca == 1:
          fin = True

      if jp.choca == 2:
          ganar = True

      if not pausa:
        if not fin:
          nivel1.Dibujar(pantalla)
          todos.update()
          todos.draw(pantalla)
          pygame.display.flip()


        else:
          if not ganar:
            nivel1.Dibujar(pantalla)
            pantalla.blit(texto,[ALTO/2,300])
            pygame.display.flip()
            time.sleep(3)

        if ganar:

          pantalla.blit(gano,[ALTO/2,300])
          pygame.display.flip()
          time.sleep(1)
          pantalla.fill(NEGRO)
          pantalla.blit(nivel2,[ALTO/2,300])
          pygame.display.flip()
          time.sleep(1)
          ganar = False
          pygame.init()
          pantalla=pygame.display.set_mode([ANCHO+125,ALTO])

          pantalla.blit(mensaje("Porcentaje de vida",20),[1023,180])
          pantalla.blit(mensaje("100",50),[1050,300])

          todos=pygame.sprite.Group()
          muere = pygame.sprite.Group()
          muros = pygame.sprite.Group()
          puertas = pygame.sprite.Group()

          nivel1 = Nivel('nivel1.map', muros, muere, puertas)
          muros = nivel1.Muros_ls()
          muere = nivel1.Muere_ls()
          puertas = nivel1.Puerta_ls()
          nivel1.Dibujar(pantalla)

          jp=Jugador2(32,32)
          todos.add(jp)
          jp.ls_muros = muros


          ts = pygame.sprite.Group()
          t = puerta_n2(448,288)
          ts.add(t)
          todos.add(t)
          jp.ls_puerta1 = ts

          n=32
          tesoros = pygame.sprite.Group()
          list_tesoros=[[5*n,6*n],[10*n,14*n],[23*n,15*n],[16*n,12*n]]
          for i in range(4):
              x = list_tesoros[i][0]
              y = list_tesoros[i][1]
              tr= tesoro(x,y)
              tesoros.add(tr)
              todos.add(tr)
          jp.ls_tesoro=tesoros

          cen=[[3*n,15*n],[3*n,6*n],[6*n,5*n],[15*n,17*n],[4*n,15*n],[13*n,17*n],[10*n,9*n],
               [21*n,8*n],[15*n,2*n],[10*n,17*n],[30*n,15*n],[28*n,14*n],[5*n,9*n],[22*n,18*n],[18*n,11*n],[18*n,18*17],
               [22*n,12*n],[25*n,12*n],[27*n,19*n]]

          enemigos = pygame.sprite.Group()
          for i in range(19):
              x = cen[i][0]
              y = cen[i][1]
              e = Enemigo(1,1,1)
              e.rect.x = x
              e.rect.y = y
              e.vel = 1
              enemigos.add(e)
              todos.add(e)
              e.ls_muros = muros
          enemigo_f = pygame.sprite.Group()
          en=Enemigo2()
          en.rect.x = 950
          en.rect.y = 96
          enemigo_f.add(en)
          todos.add(en)
          en.ls_muros = muros
          jp.ls_enem2 = enemigo_f
          jp.ls_enem = enemigos
          jp.ls_muere = muere
          jp.ls_puerta = puertas

      else:
        nivel1.Dibujar(pantalla)
        todos.draw(pantalla)
        pygame.display.flip()
