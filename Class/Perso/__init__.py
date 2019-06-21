import inspect
from os import path
import numpy as np
import os, inspect
import pygame

# recherche du répertoire de travail
scriptPATH = path.abspath(inspect.getsourcefile(lambda: 0))  # compatible interactive Python Shell
scriptDIR = path.dirname(scriptPATH)
scriptDIR = path.dirname(scriptPATH[0])
scriptDIR = path.split(scriptDIR)[0]
assets = path.join(scriptDIR, "data")

planche_sprites = pygame.image.load(os.path.join(assets, "barham.png"))

def ChargeSerieSprites(i):
   sprite = []
   if(i==0):
       spr = planche_sprites.subsurface((227, 142, 19,35))
       # point de départ en x, point de départ en y, taille de la coupure en x, taille de la coupure en y,
   if(i==1):
       spr = planche_sprites.subsurface((246, 142, 19,35))
   if(i==2):
       spr = planche_sprites.subsurface((266, 142, 19,35))
   if(i==3):
       spr = planche_sprites.subsurface((285, 142, 19,35))
   if(i==4):
       spr = planche_sprites.subsurface((304, 142, 19,35))

   if(i==5):
       spr = planche_sprites.subsurface((342, 142, 19,35))
   if(i==6):
       spr = planche_sprites.subsurface((361, 142, 19,35))
   if(i==7):
       spr = planche_sprites.subsurface((381, 142, 19,35))
   if(i==8):
       spr = planche_sprites.subsurface((400, 142, 19,35))
   if(i==9):
       spr = planche_sprites.subsurface((419, 142, 19,35))
   sprite.append( spr )
   return sprite

class Perso:
    def __init__(self, px, py, p_image):
        self.aX = px
        self.aY = py
        if p_image != "null":
            self.aImage = pygame.image.load(path.join(assets, p_image))
        else:
            self.aImage = pygame.image.load(path.join(assets, "nug.jpg"))


class Pnj(Perso):
    def __init__(self, px, py, p_image, p_dialogue, p_name):
        Perso.__init__(self, px, py, p_image)
        self.aDialogue = p_dialogue
        self.aImage.set_colorkey((0, 0, 0))
        self.aName = p_name

    def dialogue(self):
        print(self.aDialogue)


class PnjMouv(Pnj):
    def __init__(self, px, py, p_image, p_dialogue, p_name):
        Pnj.__init__(self, px, py, p_image, p_dialogue, p_name)
        self.vy = 1
        self.retour = 0

    def mouv(self, time):
        if self.retour == 0:

            if time % 5 == 0:
                cyrus = ChargeSerieSprites(5)
            if time % 5 == 1:
                cyrus = ChargeSerieSprites(6)
            if time % 5 == 2:
                cyrus = ChargeSerieSprites(7)
            if time % 5 == 3:
                cyrus = ChargeSerieSprites(8)
            if time % 5 == 4:
                cyrus = ChargeSerieSprites(9)
            self.aY += self.vy

        if self.aY > 350:
            self.retour = 1

        if self.retour == 1:
            if time % 5 == 0:
                cyrus = ChargeSerieSprites(0)
            if time % 5 == 1:
                cyrus = ChargeSerieSprites(1)
            if time % 5 == 2:
                cyrus = ChargeSerieSprites(2)
            if time % 5 == 3:
                cyrus = ChargeSerieSprites(3)
            if time % 5 == 4:
                cyrus = ChargeSerieSprites(4)
            self.aY -= self.vy
            if self.aY < 50:
                self.retour = 0

        return cyrus[time%len(cyrus)]


class Marchand(Perso):
    def __init__(self, px, py, p_image, p_shop):
        Perso.__init__(self, px, py, p_image)
        self.aShop = p_shop


class MarchandMagie(Marchand):
    def __init__(self, px, py, p_image, p_shop):
        Marchand.__init__(self, px, py, p_image, p_shop)

    @staticmethod
    def ckoi():
        return "MarchandMagie"


class MarchandArme(Marchand):
    def __init__(self, px, py, p_image, p_shop):
        Marchand.__init__(self, px, py, p_image, p_shop)

    @staticmethod
    def ckoi():
        return "MarchandArme"
