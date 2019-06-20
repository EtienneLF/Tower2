import inspect
from os import path

import pygame

import Class.Perso

# recherche du répertoire de travail
scriptPATH = path.abspath(inspect.getsourcefile(lambda: 0))  # compatible interactive Python Shell
scriptDIR = path.dirname(scriptPATH)
scriptDIR = path.dirname(scriptPATH[0])
scriptDIR = path.split(scriptDIR)[0]
assets = path.join(scriptDIR, "data\Hero_mouvement")


class Hero(Class.Perso.Perso):
    # Declaration des stats
    a_health = 100
    a_max_health = 100
    a_mana = 100
    a_speed = 60  # Attaque Speed : temps d'attente avant de pouvoir faire un mouvement
    a_strength_base = 25
    a_def_base = 1
    a_int_base = 1
    a_res_base = 1
    vitesse_base = 20

    a_max_weight = 1

    a_strength = 25
    a_def = 1
    a_int = 1
    a_res = 1
    vitesse = 20

    a_exp = 0
    a_lvl = 1
    a_exp_lvl_need = 10

    a_gold = 10
    a_weapon = None
    a_boot = None
    a_armor = None
    a_inventory = {}

    aAttaque_Speed = 6
    a_Duree = 0

    def __init__(self, px, py):
        Class.Perso.Perso.__init__(self, px, py, "null")
        self.aImage = pygame.image.load(path.join(assets, "Hero.jpg"))
        self.aImage = pygame.transform.scale(self.aImage, (50, 50))

    def dialogue(self, p_pnj, px, py):
        if self.aX + self.aImage.get_width() > p_pnj.aX - px and self.aX < p_pnj.aX + p_pnj.aImage.get_width() - px and self.aY + self.aImage.get_height() > p_pnj.aY - py and self.aY < p_pnj.aY + p_pnj.aImage.get_height() - py:
            return p_pnj.aName + " : " + p_pnj.aDialogue

    def ismarchand(self, p_marchand, px, py):
        if self.aX + self.aImage.get_width() > p_marchand.aX - px and self.aX < p_marchand.aX + p_marchand.aImage.get_width() - px and self.aY + self.aImage.get_height() > p_marchand.aY - py and self.aY < p_marchand.aY + p_marchand.aImage.get_height() - py :
            if p_marchand.ckoi() == "MarchandArme":
                return "MarchandArme"
            elif p_marchand.ckoi() == "MarchandMagie":
                return "MarchandMagie"

    def changei(self, p_image):
        self.aImage = pygame.image.load(path.join(assets, p_image + ".jpg"))
        self.aImage = pygame.transform.scale(self.aImage, (50, 50))

    def attaque(self):
        self.changei("HeroAtt")
        print("ATTAQUE")
        self.a_Duree = self.aAttaque_Speed

    def actustat(self):
        if self.a_weapon is not None:
            self.a_strength = self.a_weapon.a_Stat + self.a_strength_base
        if self.a_boot is not None:
            self.vitesse = self.a_boot.a_Stat + self.vitesse_base
        if self.a_armor is not None:
            self.a_def = self.a_armor.a_Stat + self.a_def_base

    def actulvl(self):
        if self.a_exp >= self.a_exp_lvl_need:
            self.a_lvl += 1
            self.a_exp = self.a_exp - self.a_exp_lvl_need
            self.a_exp_lvl_need = int(self.a_exp_lvl_need * 1.5)
            return True
        else:
            return False
