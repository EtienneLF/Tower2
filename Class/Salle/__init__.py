import inspect
import os
from os import path

import pygame

# recherche du répertoire de travail
scriptPATH = path.abspath(inspect.getsourcefile(lambda: 0))  # compatible interactive Python Shell
scriptDIR = path.dirname(scriptPATH)
scriptDIR = path.dirname(scriptPATH[0])
scriptDIR = path.split(scriptDIR)[0]
assets = path.join(scriptDIR, "data")


class Salle:

    def __init__(self, p_pnj_liste, p_mob_liste, p_item_liste, p_image, p_x_decor, p_y_decor, p_hitbox, p_sortie, p_marchand_liste):
        self.a_Pnj_List = p_pnj_liste
        self.a_Mob_List = p_mob_liste
        self.a_Item_List = p_item_liste
        self.a_Image = p_image
        self.a_XDecor = p_x_decor
        self.a_YDecor = p_y_decor
        self.a_Tab_Hitbox = p_hitbox
        self.a_Sortie_Liste = p_sortie
        self.a_Marchand_Liste = p_marchand_liste


class ChangeSalle:

    def __init__(self, px, py, p_image, p_salle, px_decor, py_decor, px_perso, py_perso):
        self.aX = px
        self.aY = py
        self.a_Image = pygame.image.load(os.path.join(assets, p_image))
        self.a_Salle = p_salle
        self.aX_Decor = px_decor
        self.aY_Decor = py_decor
        self.aX_Perso = px_perso
        self.aY_Perso = py_perso

class ChangeSalleCondi(ChangeSalle):

    def __init__(self, px, py, p_image, p_salle, px_decor, py_decor, px_perso, py_perso):
        ChangeSalle.__init__(px, py, p_image, p_salle, px_decor, py_decor, px_perso, py_perso)

