from Class.Pnj import Pnj
from Class.Hero import Hero
from Class.Mob import Mob
import os
import inspect
import pygame

class Salle:

    def __init__(self, pPnj_Liste, pMob_Liste, pItem_Liste, pimage):
        self.a_Pnj_List = pPnj_Liste
        self.a_Mob_List = pMob_Liste
        self.a_Item_List = pItem_Liste
        self.a_Image = pimage
