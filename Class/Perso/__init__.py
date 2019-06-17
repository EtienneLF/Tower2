# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 20:40:43 2019

@author: Etienne
"""
import pygame
import inspect
from os import path

# recherche du répertoire de travail
scriptPATH = path.abspath(inspect.getsourcefile(lambda: 0))  # compatible interactive Python Shell
scriptDIR = path.dirname(scriptPATH)
scriptDIR = path.dirname(scriptPATH[0])
scriptDIR = path.split(scriptDIR)[0]
assets = path.join(scriptDIR, "data")


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
        self.aName = p_name

    def dialogue(self):
        print(self.aDialogue)


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
