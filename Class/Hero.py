# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 10:03:13 2019

@author: Etienne
"""

import Class.Perso
import pygame
import inspect
from os import path

# recherche du répertoire de travail
scriptPATH = path.abspath(inspect.getsourcefile(lambda: 0))  # compatible interactive Python Shell
scriptDIR = path.dirname(scriptPATH)
scriptDIR = path.split(scriptDIR)[0]
assets = path.join(scriptDIR, "data\Hero_mouvement")


class Hero(Class.Perso.Perso):
    # Declaration des stats
    a_health = 1
    a_strength = 2
    a_speed = 60  # Attaque Speed : temps d'attente avant de pouvoir faire un mouvement
    a_mana = 1
    a_def = 1
    a_int = 1
    a_res = 1
    vitesse = 20
    a_max_weight = 1
    a_exp = 0
    a_lvl = 1
    a_weapon = None
    a_armor = None
    a_inventory = {}
    
    a_Puissance_stuff = 25
    aAttaque_Speed = 60
    aDuree = 0

    def __init__(self, px, py):
        Class.Perso.Perso.__init__(self, px, py, "null")
        self.aImage = pygame.image.load(path.join(assets, "Hero.jpg"))
        self.aImage = pygame.transform.scale(self.aImage, (100, 107))

    def dialogue(self, p_pnj, px_decor):
        if self.aX >= p_pnj.aX - px_decor:
            print(p_pnj.aDialogue)

    def changei(self, p_image):
        self.aImage = pygame.image.load(path.join(assets, p_image + ".jpg"))
        self.aImage = pygame.transform.scale(self.aImage, (100, 107))

    def attaque(self):
        self.changei("HeroAtt")
        print("ATTAQUE")
        self.aDuree = self.aAttaque_Speed
