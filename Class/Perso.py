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
scriptDIR = path.split(scriptDIR)[0]
assets = path.join(scriptDIR, "data")


class Perso:
    vitesse = 20
    
    def __init__(self, px, py, p_image):
        self.aX = px
        self.aY = py
        if p_image != "null":
            self.aImage = pygame.image.load(path.join(assets, p_image))
        else:
            self.aImage = pygame.image.load(path.join(assets, "nug.jpg"))


class Pnj(Perso):
    def __init__(self, px, py, p_image, p_dialogue):
        Perso.__init__(self, px, py, p_image)
        self.aDialogue = p_dialogue

    def dialogue(self):
        print(self.aDialogue)