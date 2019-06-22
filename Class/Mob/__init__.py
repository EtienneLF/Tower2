import random
from os import path
import os, inspect
import pygame
import Class.Perso


# recherche du répertoire de travail
scriptPATH = path.abspath(inspect.getsourcefile(lambda: 0))  # compatible interactive Python Shell
scriptDIR = path.dirname(scriptPATH)
scriptDIR = path.dirname(scriptPATH[0])
scriptDIR = path.split(scriptDIR)[0]
assets = path.join(scriptDIR, "data")


planche_sprites = pygame.image.load(os.path.join(assets, "Darknut.png"))
planche_sprites.set_colorkey((0,128,255))

planche_sprite = pygame.image.load(os.path.join(assets, "DarkLink.png"))
planche_sprite.set_colorkey((184,184,184))


def EnnemiSprite(nb,id,dec_x,dec_y,tai_x,tai_y):
   sprite = []
   for i in range(nb):
      spr = planche_sprites.subsurface((tai_x * i + dec_x , tai_y * id + dec_y , tai_x,tai_y))
      test = spr.get_at((10,10))
      if ( test != (255,0,0,255) ):
         sprite.append( spr )
   return sprite


def BossSprite(nb,id,dec_x,dec_y,tai_x,tai_y):
   sprite = []
   for i in range(nb):
      spr = planche_sprite.subsurface((tai_x * i + dec_x , tai_y * id + dec_y , tai_x,tai_y))
      test = spr.get_at((10,10))
      if ( test != (255,0,0,255) ):
         sprite.append( spr )
   return sprite

dep_H = EnnemiSprite(4,0,5,10,31,44)
dep_D = EnnemiSprite(4,1,4,10,29,44)
dep_B = EnnemiSprite(4,2,3,6,29,44)
dep_G = EnnemiSprite(4,3,0,6,29,44)

Bdep_H = BossSprite(6, 0, 3, 3, 33, 30)
Bdep_G = BossSprite(6, 1, 3, 3, 32, 30)
Bdep_B = BossSprite(6, 2, 3, 3, 32, 30)
Bdep_D = BossSprite(6, 3, 3, 3, 32, 30)


class Mob(Class.Perso.Perso):
    def __init__(self, px, py, p_health, p_image, p_vitesse, p_distance, p_xp, p_attaque):
        Class.Perso.Perso.__init__(self, px, py, p_image)
        self.a_health = p_health
        self.a_vitesse = p_vitesse
        self.d_X = 0
        self.d_Y = 0
        self.temps = 0
        self.tempsAttaque = 1
        self.distance = p_distance
        self.xp = p_xp
        self.attack = p_attaque
        self.mode_a = False
        self.gold = 5
        self.aEtat = dep_B

    def getattack(self, p_hero, p_x, p_y):
        if self.aX - 10 < p_hero.aX + p_x < self.aX + 33 + 10 and self.aY - 10 < p_hero.aY + p_y < self.aY + 35 + 10:
            print("Dégats infligés =" + str(p_hero.a_strength))
            self.a_health -= p_hero.a_strength

    def attaque(self, p_hero, p_x, p_y):
        if self.tempsAttaque <= 0:
            if p_hero.aX + p_x + 40 >= self.aX and p_hero.aX + p_x < self.aX + 40 and p_hero.aY + p_y < self.aY + 40 and p_hero.aY + p_y + 40 > self.aY :
                p_hero.a_health -= self.attack - int(p_hero.a_def /5)
                print("Dégats subis =" + str(self.attack - int(p_hero.a_def /5)))
                self.tempsAttaque = 30
            else:
                self.tempsAttaque = 0
        else:
            self.tempsAttaque -= 1

    def random_move(self):
        move_x = random.randint(0, 2)
        move_y = random.randint(0, 2)
        if move_x == 1:
            self.d_X = self.a_vitesse
            self.aEtat = dep_D
        elif move_x == 2:
            self.d_X = -self.a_vitesse
            self.aEtat = dep_G
        else:
            self.d_X = 0
        if move_y == 1:
            self.d_Y = self.a_vitesse
            if self.d_X == 0:
                self.aEtat = dep_B
        elif move_y == 2:
            self.d_Y = -self.a_vitesse
            if self.d_X == 0:
                self.aEtat = dep_H
        else:
            self.d_Y = 0

    def move(self, p_x, p_y):
        if self.aX - self.distance < p_x < self.aX + self.aImage.get_width() + self.distance and self.aY - self.distance < p_y < self.aY + self.aImage.get_height() + self.distance:
            self.mode_a = True
        if self.mode_a:
            if self.aX < p_x:
                self.d_X = self.a_vitesse
                self.aEtat = dep_D
                if self.aX + self.d_X > p_x:
                    self.d_X = 0
                    self.aX = p_x
            elif self.aX > p_x:
                self.d_X = -self.a_vitesse
                self.aEtat = dep_G
                if self.aX + self.d_X< p_x:
                    self.d_X = 0
                    self.aX = p_x
            else:
                self.d_X = 0

            if self.aY < p_y:
                self.d_Y = self.a_vitesse
                if self.d_X == 0:
                    self.aEtat = dep_B
                if self.aY + self.d_Y > p_y:
                    self.d_Y = 0
                    self.aY = p_y
            elif self.aY > p_y:
                self.d_Y = -self.a_vitesse
                if self.d_X == 0:
                    self.aEtat = dep_H
                if self.aY + self.d_Y< p_y:
                    self.d_Y = 0
                    self.aY = p_y
            else:
                self.d_Y = 0

            self.aX += self.d_X
            self.aY += self.d_Y
        else:
            if self.temps > 0:
                self.aX += self.d_X
                self.aY += self.d_Y
                self.temps -= 1
            else:
                self.random_move()
                self.temps = 30

    def imagequel(self,time):
        if self.aEtat == dep_D :
            return dep_D[time%len(dep_D)]
        elif self.aEtat == dep_G :
            return dep_G[time%len(dep_G)]
        elif self.aEtat == dep_B :
            return dep_B[time%len(dep_B)]
        elif self.aEtat == dep_H :
            return dep_H[time%len(dep_H)]


class Boss(Mob):
    def __init__(self, px, py, p_health, p_image, p_vitesse, p_distance, p_xp, p_attaque):
        Mob.__init__(self, px, py, p_health, p_image, p_vitesse, p_distance, p_xp, p_attaque)
        self.aEtat = Bdep_B

    def random_move(self):
        move_x = random.randint(0, 2)
        move_y = random.randint(0, 2)
        if move_x == 1:
            self.d_X = self.a_vitesse
            self.aEtat = Bdep_D
        elif move_x == 2:
            self.d_X = -self.a_vitesse
            self.aEtat = Bdep_G
        else:
            self.d_X = 0
        if move_y == 1:
            self.d_Y = self.a_vitesse
            if self.d_X == 0:
                self.aEtat = Bdep_B
        elif move_y == 2:
            self.d_Y = -self.a_vitesse
            if self.d_X == 0:
                self.aEtat = Bdep_H
        else:
            self.d_Y = 0

    def move(self, p_x, p_y):
        if self.aX - self.distance < p_x < self.aX + self.aImage.get_width() + self.distance and self.aY - self.distance < p_y < self.aY + self.aImage.get_height() + self.distance:
            self.mode_a = True
        if self.mode_a:
            if self.aX < p_x:
                self.d_X = self.a_vitesse
                self.aEtat = Bdep_D
                if self.aX + self.d_X> p_x:
                    self.d_X = 0
                    self.aX = p_x
            elif self.aX > p_x:
                self.d_X = -self.a_vitesse
                self.aEtat = Bdep_G
                if self.aX + self.d_X< p_x:
                    self.d_X = 0
                    self.aX = p_x
            else:
                self.d_X = 0

            if self.aY < p_y:
                self.d_Y = self.a_vitesse
                if self.d_X == 0:
                    self.aEtat = Bdep_B
                if self.aY + self.d_Y > p_y:
                    self.d_Y = 0
                    self.aY = p_y
            elif self.aY > p_y:
                self.d_Y = -self.a_vitesse
                if self.d_X == 0:
                    self.aEtat = Bdep_H
                if self.aY + self.d_Y< p_y:
                    self.d_Y = 0
                    self.aY = p_y
            else:
                self.d_Y = 0

            self.aX += self.d_X
            self.aY += self.d_Y
        else:
            if self.temps > 0:
                self.aX += self.d_X
                self.aY += self.d_Y
                self.temps -= 1
            else:
                self.random_move()
                self.temps = 30

    def imagequel(self,time):
        if self.aEtat == Bdep_D :
            return Bdep_D[time%len(Bdep_D)]
        elif self.aEtat == Bdep_G :
            return Bdep_G[time%len(Bdep_G)]
        elif self.aEtat == Bdep_B :
            return Bdep_B[time%len(Bdep_B)]
        elif self.aEtat == Bdep_H :
            return Bdep_H[time%len(Bdep_H)]