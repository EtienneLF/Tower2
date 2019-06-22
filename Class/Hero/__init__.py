import inspect
import os
from os import path
import pygame
from pygame.transform import scale
import Class.Perso

# recherche du répertoire de travail
scriptPATH = path.abspath(inspect.getsourcefile(lambda: 0))  # compatible interactive Python Shell
scriptDIR = path.dirname(scriptPATH)
scriptDIR = path.dirname(scriptPATH[0])
scriptDIR = path.split(scriptDIR)[0]
assets = path.join(scriptDIR, "data")

planche_sprites = pygame.image.load(os.path.join(assets, "protag.png"))
planche_sprites.set_colorkey((0, 0, 0))

planche_sprites_femme = pygame.image.load(os.path.join(assets, "robinf3.png"))
planche_sprites_femme.set_colorkey((0, 0, 0))


def hero_sprite(id, color):
    sprite = []
    for i in range(4):
        spr = planche_sprites.subsurface((33 * i + 129 * color, 33 * id , 35,33))
        test = spr.get_at((10,10))
        if test != (255,0,0,255) :
            sprite.append( spr )
    return sprite


LARG = 63
LONG = 64
# Color R = 0 ; Color B = 1 ; Color V = 2
def ChargeSerieSprites(id, col):
   sprite = []
   for i in range(4):
        dt = LARG * i
        spr = planche_sprites_femme.subsurface((dt+col*(4*LARG)+i, LARG * id + 2 + id, LARG,LONG))
        test = spr.get_at((int(LARG/2),int(LONG/2)))
        if (test != (0,0,0,255)):
            sprite.append( spr )
   return sprite



Bas = 00
Gauche = 1
Haut = 2
Droite = 3

Attaque = 5
Idle = 6
Marche = 7

Homme = 10
Femme = 20

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
    vitesse_base = 5
    a_genre = 0

    a_max_weight = 1

    a_strength = 25
    a_def = 1
    a_int = 1
    a_res = 1
    vitesse = 5

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

    a_dir = Bas
    a_Etat = Idle
    a_etat = "marche"

    a_genre = Femme

    a_color = 1

    def __init__(self, px, py):
        Class.Perso.Perso.__init__(self, px, py, "null")
        self.updatesprite()

    def dialogue(self, p_pnj, px, py):
        if self.aX + 35 > p_pnj.aX - px and self.aX < p_pnj.aX + 43 - px and self.aY + 43 > p_pnj.aY - py and self.aY < p_pnj.aY + 43 - py:
            return p_pnj.aName + " : " + p_pnj.aDialogue

    def ismarchand(self, p_marchand, px, py):
        if self.aX + 35 > p_marchand.aX - px - 150 and self.aX < p_marchand.aX + 150 - px and self.aY + 33 > p_marchand.aY - py - 150 and self.aY < p_marchand.aY + 150 - py :
            if p_marchand.ckoi() == "MarchandArme":
                return "MarchandArme"
            elif p_marchand.ckoi() == "MarchandMagie":
                return "MarchandMagie"

    def updatesprite(self):
        if self.a_genre == Homme:
            self.a_idle = hero_sprite(0, self.a_color)
            self.a_attG = hero_sprite(1, self.a_color)
            self.depG = hero_sprite(2, self.a_color)
            self.aDepD = hero_sprite(3, self.a_color)
            self.a_DepB = hero_sprite(4, self.a_color)
            self.aDepH = hero_sprite(5, self.a_color)
            self.a_attD = hero_sprite(10, self.a_color)
        else:

            self.a_idle = ChargeSerieSprites(0, self.a_color)
            self.a_attG = ChargeSerieSprites(1, self.a_color)
            self.depG = ChargeSerieSprites(2, self.a_color)
            self.aDepD = ChargeSerieSprites(3, self.a_color)
            self.a_DepB = ChargeSerieSprites(4, self.a_color)
            self.aDepH = ChargeSerieSprites(5, self.a_color)
            self.a_attD = None

    def attaque(self):
        self.a_Etat = Attaque
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

    def quelimage(self,time):
        if self.a_Etat == Idle:
            return scale(self.a_idle[time % len(self.a_idle)],(35,33))
        elif self.a_Etat == Marche:
            if self.a_dir == Bas:
                return scale(self.a_DepB[time%len(self.a_DepB)],(35,33))
            elif self.a_dir == Haut:
                return scale(self.aDepH[time%len(self.aDepH)],(35,33))
            elif self.a_dir == Gauche:
                return scale(self.depG[time%len(self.depG)],(35,33))
            elif self.a_dir == Droite:
                return scale(self.aDepD[time%len(self.aDepD)],(35,33))
        elif self.a_Etat == Attaque:
            if self.a_dir == Droite:
                return pygame.transform.flip( scale(self.a_attG[time % len(self.a_attG)],(35,33)), True, False)
            elif self.a_dir == Gauche:
                return scale(self.a_attG[time%len(self.a_attG)],(35,33))
            elif self.a_dir == Bas:
                return scale(self.a_DepB[time%len(self.a_DepB)],(35,33))
            elif self.a_dir == Haut:
                return scale(self.aDepH[time%len(self.aDepH)],(35,33))
