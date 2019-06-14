from Class.Hero import Hero
from Class.Mob import Mob
import os
import inspect
import pygame

class Salle:

    def __init__(self, pPnj_Liste, pMob_Liste, pItem_Liste, pimage, p_xdecor, p_ydecor, phitbox):
        self.a_Pnj_List = pPnj_Liste
        self.a_Mob_List = pMob_Liste
        self.a_Item_List = pItem_Liste
        self.a_Image = pimage
        self.a_XDecor = p_xdecor
        self.a_YDecor = p_ydecor
        self.a_Tab_Hitbox = phitbox
