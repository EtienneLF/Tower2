import inspect
import time as temps
import os
import pygame
from Class.Button import Button_lvl
from Class.Cailloux import Cailloux
from Class.Hero import Hero
from Class.Item import Epee, Bottes, Armure
from Class.Mob import Mob, Boss
from Class.Perso import Pnj, MarchandArme, MarchandMagie, PnjMouv
from Class.Salle import Salle, ChangeSalle
from Class.Shop import Shop

# recherche du repertoire de travail bonjour

scriptPATH = os.path.abspath(inspect.getsourcefile(lambda: 0))  # compatible interactive Python Shell
scriptDIR = os.path.dirname(scriptPATH)
assets = os.path.join(scriptDIR, "data")
sound = os.path.join(scriptDIR, "sound")
music = os.path.join(scriptDIR, "music")

pygame.mixer.pre_init(44100, 16, 2, 4096)

# Image du title screen
Title_Screen = pygame.image.load(os.path.join(assets, "TitleScreenV1.png"))

Selection_Screen = pygame.image.load(os.path.join(assets, "Selection de sexe.png"))

Couleur_Screen = pygame.image.load(os.path.join(assets, "Selection Couleur.png"))

# Charge les images des différentes map
Map_Base_Image = pygame.image.load(os.path.join(assets, "cités.png"))
Map_Glace_Image = pygame.image.load(os.path.join(assets, "Glace.PNG"))
Shop1_Image = pygame.image.load(os.path.join(assets, "shop1.png"))
Shop2_Image = pygame.image.load(os.path.join(assets, "shop2.png"))
Plaine_Image = pygame.image.load(os.path.join(assets, "Plaine.png"))
Glace2_Image = pygame.image.load(os.path.join(assets, "Glace2.png"))
Boss_Image = pygame.image.load(os.path.join(assets, "Boss.png"))

# Création équipement
Excalibur = Epee("Epee basique", 5, 10, "Un bon équipement de premier prix")
Excalibur.a_Image = pygame.image.load(os.path.join(assets, "épée1.png"))
Excalibur.a_Image = pygame.transform.scale(Excalibur.a_Image, (100, 100))

Tee_shirt = Armure("Armure ", 5, 10, "Peut vous protéger des coups les moins forts")
Tee_shirt.a_Image = pygame.image.load(os.path.join(assets, "armure1.png"))
Tee_shirt.a_Image = pygame.transform.scale(Tee_shirt.a_Image, (100, 100))

Sandales = Bottes("Bottes", 5, 2, "Vous permet d'augmenter un petit peu votre vitesse")
Sandales.a_Image = pygame.image.load(os.path.join(assets, "botte1.png"))
Sandales.a_Image = pygame.transform.scale(Sandales.a_Image, (100, 100))

Excalibur2 = Epee("Epee Magique", 10, 20, "Une excellente épée faite pour les meilleurs")
Excalibur2.a_Image = pygame.image.load(os.path.join(assets, "épée2.png"))
Excalibur2.a_Image = pygame.transform.scale(Excalibur.a_Image, (100, 100))

Armure2 = Armure("Armure Enchantée", 10, 20, "Permet de réduire considérablement les dégâts subit")
Armure2.a_Image = pygame.image.load(os.path.join(assets, "armure1.png"))
Armure2.a_Image = pygame.transform.scale(Tee_shirt.a_Image, (100, 100))

Bottesa = Bottes("Bottes Ailées", 10, 6, "Permet de courir sans effort")
Bottesa.a_Image = pygame.image.load(os.path.join(assets, "botte1.png"))
Bottesa.a_Image = pygame.transform.scale(Sandales.a_Image, (100, 100))

# Création Shop
Shop_Arme_Base = Shop(Excalibur, Tee_shirt, Sandales)

Shop_Magie_Base = Shop(Excalibur2, Armure2, Bottesa)

# Création marchant
Marchand_Arme = MarchandArme(341, 218, "Marchand_Arme.png", Shop_Arme_Base)

Marchand_Magie = MarchandMagie(490, 335, "Marchand_Magie.png", Shop_Magie_Base)

# Pnj
Megumin = PnjMouv(620, 545, "Megumin.png", "Bonjour", "Habitant")

# Mob
Mob_1 = Mob(90, 790, 100, "Megumin.png", 2, 100, 10, 5)
Mob_2 = Mob(275, 55, 100, "Megumin.png", 2, 100, 10, 5)
Mob_3 = Mob(900, 900, 100, "Megumin.png", 2, 100, 10, 5)
Mob_4 = Mob(553, 813, 100, "Megumin.png", 2, 100, 10, 5)
Mob_5 = Mob(790, 790, 100, "Megumin.png", 2, 100, 10, 5)
Mob_6 = Mob(830, 400, 100, "Megumin.png", 2, 100, 10, 5)
Mob_7 = Mob(210, 890, 100, "Megumin.png", 2, 100, 10, 5)
Mob_8 = Mob(441, 161, 100, "Megumin.png", 2, 100, 10, 5)

Boss_mob = Boss(400, 400, 300, "Megumin.png", 4, 300, 40, 30)

# Création cailloux

Glace_Cailloux1 = Cailloux(303, 297)
Glace_Cailloux2 = Cailloux(423, 356)
Glace_Cailloux3 = Cailloux(475, 409)
Glace_Cailloux4 = Cailloux(65, 349)
Glace_Cailloux5 = Cailloux(241, 472)
Glace_Cailloux6 = Cailloux(650, 472)
Glace_Cailloux7 = Cailloux(828, 62)
Glace_Cailloux8 = Cailloux(886, 296)
Glace_Cailloux9 = Cailloux(418, 588)
Glace_Cailloux10 = Cailloux(535, 588)
Glace_Cailloux11 = Cailloux(652, 588)
Glace_Cailloux12 = Cailloux(300, 588)
Glace_Cailloux13 = Cailloux(944, 117)
Glace_Cailloux14 = Cailloux(241, 4)
Glace_Cailloux15 = Cailloux(299, 63)
Glace_Cailloux16 = Cailloux(361, 120)
Glace_Cailloux17 = Cailloux(421, 182)
Glace_Cailloux18 = Cailloux(535, 182)
Glace_Cailloux19 = Cailloux(593, 120)
Glace_Cailloux20 = Cailloux(652, 63)
Glace_Cailloux21 = Cailloux(711, 4)
Glace_Cailloux22 = Cailloux(945, 409)
Glace_Cailloux23 = Cailloux(886, 530)
Glace_Cailloux24 = Cailloux(593, 640)
Glace_Cailloux25 = Cailloux(361, 640)
Glace_Cailloux26 = Cailloux(125, 588)
Glace_Cailloux27 = Cailloux(125, 642)
Glace_Cailloux28 = Cailloux(828, 645)
Glace_Cailloux29 = Cailloux(299, 1)
Glace_Cailloux30 = Cailloux(361, 56)
Glace_Cailloux31 = Cailloux(652, 1)
Glace_Cailloux32 = Cailloux(593, 56)
Glace_Cailloux33 = Cailloux(241, 588)
Glace_Cailloux34 = Cailloux(241, 635)
Glace_Cailloux35 = Cailloux(705, 588)
Glace_Cailloux36 = Cailloux(705, 635)
Glace_Cailloux37 = Cailloux(180, 646)
Glace_Cailloux38 = Cailloux(180, 704)
Glace_Cailloux39 = Cailloux(768, 646)
Glace_Cailloux40 = Cailloux(768, 704)

ville_pub1 = Cailloux(387, 185)
ville_pub2 = Cailloux(387, 234)
ville_pub3 = Cailloux(437, 185)
ville_pub4 = Cailloux(475, 185)
ville_pub5 = Cailloux(436, 234)
ville_pub6 = Cailloux(475, 234)

ville_guilde1 = Cailloux(663, 156)
ville_guilde2 = Cailloux(712, 156)
ville_guilde3 = Cailloux(761, 156)
ville_guilde4 = Cailloux(805, 156)
ville_guilde5 = Cailloux(663, 215)
ville_guilde6 = Cailloux(663, 260)
ville_guilde7 = Cailloux(712, 260)
ville_guilde8 = Cailloux(761, 260)
ville_guilde9 = Cailloux(805, 260)
ville_guilde10 = Cailloux(805, 215)

ville_shop1 = Cailloux(219, 402)
ville_shop2 = Cailloux(268, 402)
ville_shop3 = Cailloux(318, 402)
ville_shop4 = Cailloux(368, 402)
ville_shop5 = Cailloux(418, 402)
ville_shop6 = Cailloux(468, 402)
ville_shop7 = Cailloux(475, 402)
ville_shop8 = Cailloux(220, 450)
ville_shop9 = Cailloux(270, 450)
ville_shop10 = Cailloux(320, 450)
ville_shop11 = Cailloux(370, 450)
ville_shop12 = Cailloux(420, 450)
ville_shop13 = Cailloux(470, 450)
ville_shop14 = Cailloux(475, 450)

ville_maison1 = Cailloux(167, 47)
ville_maison2 = Cailloux(217, 47)
ville_maison3 = Cailloux(255, 47)
ville_maison4 = Cailloux(167, 107)
ville_maison5 = Cailloux(255, 107)
ville_maison6 = Cailloux(167, 167)
ville_maison7 = Cailloux(255, 167)
ville_maison8 = Cailloux(167, 224)
ville_maison9 = Cailloux(255, 224)
ville_maison10 = Cailloux(167, 233)
ville_maison11 = Cailloux(217, 233)
ville_maison12 = Cailloux(255, 233)

ville_eau1 = Cailloux(935, 451)
ville_eau2 = Cailloux(950, 451)

ville_cite1 = Cailloux(281, 639)
ville_cite2 = Cailloux(281, 580)
ville_cite3 = Cailloux(232, 580)
ville_cite4 = Cailloux(183, 580)
ville_cite5 = Cailloux(133, 580)
ville_cite6 = Cailloux(83, 580)
ville_cite7 = Cailloux(33, 580)
ville_cite8 = Cailloux(1, 521)
ville_cite9 = Cailloux(1, 461)
ville_cite10 = Cailloux(1, 401)
ville_cite11 = Cailloux(1, 341)
ville_cite12 = Cailloux(1, 281)
ville_cite13 = Cailloux(1, 221)
ville_cite14 = Cailloux(35, 108)
ville_cite15 = Cailloux(83, 64)
ville_cite16 = Cailloux(132, 64)
ville_cite17 = Cailloux(162, 109)
ville_cite18 = Cailloux(211, 65)
ville_cite19 = Cailloux(261, 65)
ville_cite20 = Cailloux(311, 65)
ville_cite21 = Cailloux(361, 65)
ville_cite22 = Cailloux(411, 65)
ville_cite23 = Cailloux(458, 65)
ville_cite24 = Cailloux(490, 109)
ville_cite25 = Cailloux(539, 65)
ville_cite26 = Cailloux(589, 65)
ville_cite27 = Cailloux(614, 109)
ville_cite28 = Cailloux(652, 168)
ville_cite29 = Cailloux(652, 228)
ville_cite30 = Cailloux(652, 288)
ville_cite31 = Cailloux(652, 348)
ville_cite32 = Cailloux(652, 408)
ville_cite33 = Cailloux(652, 468)
ville_cite34 = Cailloux(602, 493)
ville_cite35 = Cailloux(574, 533)
ville_cite36 = Cailloux(525, 580)
ville_cite37 = Cailloux(475, 580)
ville_cite38 = Cailloux(425, 580)
ville_cite39 = Cailloux(375, 580)
ville_cite40 = Cailloux(375, 639)
ville_cite41 = Cailloux(205, 248)
ville_cite42 = Cailloux(255, 248)
ville_cite43 = Cailloux(305, 248)
ville_cite44 = Cailloux(355, 248)
ville_cite45 = Cailloux(405, 248)
ville_cite46 = Cailloux(444, 248)
#ville_cite47 = Cailloux(326, 227)
ville_cite48 = Cailloux(326, 166)
ville_cite49 = Cailloux(205, 308)
ville_cite50 = Cailloux(205, 325)
ville_cite51 = Cailloux(255, 325)
ville_cite52 = Cailloux(305, 325)
ville_cite53 = Cailloux(355, 325)
ville_cite54 = Cailloux(405, 325)
ville_cite55 = Cailloux(444, 325)
ville_cite56 = Cailloux(1, 156)

shop_magie_Cailloux1 = Cailloux(0,0)
shop_magie_Cailloux2 = Cailloux(50,0)
shop_magie_Cailloux3 = Cailloux(100,0)
shop_magie_Cailloux4 = Cailloux(150,0)
shop_magie_Cailloux5 = Cailloux(200,0)
shop_magie_Cailloux6 = Cailloux(250,0)
shop_magie_Cailloux7 = Cailloux(300,0)
shop_magie_Cailloux8 = Cailloux(350,0)
shop_magie_Cailloux9 = Cailloux(400,0)
shop_magie_Cailloux10 = Cailloux(450,0)
shop_magie_Cailloux11 = Cailloux(500,0)
shop_magie_Cailloux12 = Cailloux(550,0)
shop_magie_Cailloux13 = Cailloux(600,0)
shop_magie_Cailloux14 = Cailloux(650,0)
shop_magie_Cailloux15 = Cailloux(700,0)
shop_magie_Cailloux16 = Cailloux(750,0)
shop_magie_Cailloux17 = Cailloux(800,0)
shop_magie_Cailloux18 = Cailloux(850,0)
shop_magie_Cailloux19 = Cailloux(900,0)
shop_magie_Cailloux20 = Cailloux(950,0)
shop_magie_Cailloux21 = Cailloux(1000,0)
shop_magie_Cailloux22 = Cailloux(0,60)
shop_magie_Cailloux23 = Cailloux(50,60)
shop_magie_Cailloux24 = Cailloux(100,60)
shop_magie_Cailloux25 = Cailloux(150,60)
shop_magie_Cailloux26 = Cailloux(200,60)
shop_magie_Cailloux27 = Cailloux(250,60)
shop_magie_Cailloux28 = Cailloux(300,60)
shop_magie_Cailloux29 = Cailloux(350,60)
shop_magie_Cailloux30 = Cailloux(400,60)
shop_magie_Cailloux31 = Cailloux(450,60)
shop_magie_Cailloux32 = Cailloux(500,60)
shop_magie_Cailloux33 = Cailloux(550,60)
shop_magie_Cailloux34 = Cailloux(600,60)
shop_magie_Cailloux35 = Cailloux(650,60)
shop_magie_Cailloux36 = Cailloux(700,60)
shop_magie_Cailloux37 = Cailloux(750,60)
shop_magie_Cailloux38 = Cailloux(800,60)
shop_magie_Cailloux39 = Cailloux(850,60)
shop_magie_Cailloux40 = Cailloux(900,60)
shop_magie_Cailloux41 = Cailloux(950,60)
shop_magie_Cailloux42 = Cailloux(1000,60)
shop_magie_Cailloux43 = Cailloux(0,120)
shop_magie_Cailloux44 = Cailloux(50,120)
shop_magie_Cailloux45 = Cailloux(100,120)
shop_magie_Cailloux46 = Cailloux(150,120)
shop_magie_Cailloux47 = Cailloux(200,120)
shop_magie_Cailloux48 = Cailloux(250,120)
shop_magie_Cailloux49 = Cailloux(300,120)
shop_magie_Cailloux50 = Cailloux(350,120)
shop_magie_Cailloux51 = Cailloux(400,120)
shop_magie_Cailloux52 = Cailloux(450,120)
shop_magie_Cailloux53 = Cailloux(500,120)
shop_magie_Cailloux54 = Cailloux(550,120)
shop_magie_Cailloux55 = Cailloux(600,120)
shop_magie_Cailloux56 = Cailloux(650,120)
shop_magie_Cailloux57 = Cailloux(700,120)
shop_magie_Cailloux58 = Cailloux(750,120)
shop_magie_Cailloux59 = Cailloux(800,120)
shop_magie_Cailloux60 = Cailloux(850,120)
shop_magie_Cailloux61 = Cailloux(900,120)
shop_magie_Cailloux62 = Cailloux(950,120)
shop_magie_Cailloux63 = Cailloux(950,120)
shop_magie_Cailloux64 = Cailloux(0,180)
shop_magie_Cailloux65 = Cailloux(0,240)
shop_magie_Cailloux66 = Cailloux(0,300)
shop_magie_Cailloux67 = Cailloux(0,360)
shop_magie_Cailloux68 = Cailloux(0,420)
shop_magie_Cailloux69 = Cailloux(0,480)
shop_magie_Cailloux70 = Cailloux(0,540)
shop_magie_Cailloux71 = Cailloux(0,600)
shop_magie_Cailloux72 = Cailloux(0,660)
shop_magie_Cailloux73 = Cailloux(0,720)
shop_magie_Cailloux74 = Cailloux(0,780)
shop_magie_Cailloux75 = Cailloux(0,840)
shop_magie_Cailloux76 = Cailloux(0,900)
shop_magie_Cailloux77 = Cailloux(0,960)
shop_magie_Cailloux78 = Cailloux(0,1020)
shop_magie_Cailloux79 = Cailloux(50,720)
shop_magie_Cailloux80 = Cailloux(100,720)
shop_magie_Cailloux81 = Cailloux(150,720)
shop_magie_Cailloux82 = Cailloux(200,720)
shop_magie_Cailloux83 = Cailloux(250,720)
shop_magie_Cailloux84 = Cailloux(300,720)
shop_magie_Cailloux85 = Cailloux(350,720)
shop_magie_Cailloux86 = Cailloux(400,720)
shop_magie_Cailloux87 = Cailloux(430,720)
shop_magie_Cailloux88 = Cailloux(430,720)
shop_magie_Cailloux89 = Cailloux(430,780)
shop_magie_Cailloux90 = Cailloux(0,780)
shop_magie_Cailloux91 = Cailloux(430,780)
shop_magie_Cailloux92 = Cailloux(0,780)
shop_magie_Cailloux93 = Cailloux(50,780)
shop_magie_Cailloux94 = Cailloux(100,780)
shop_magie_Cailloux95 = Cailloux(150,780)
shop_magie_Cailloux96 = Cailloux(200,780)
shop_magie_Cailloux97 = Cailloux(530,720)
shop_magie_Cailloux98 = Cailloux(530,780)
shop_magie_Cailloux99 = Cailloux(580,720)
shop_magie_Cailloux100 = Cailloux(630,720)
shop_magie_Cailloux101 = Cailloux(680,720)
shop_magie_Cailloux102 = Cailloux(730,720)
shop_magie_Cailloux103 = Cailloux(780,720)
shop_magie_Cailloux104 = Cailloux(830,720)
shop_magie_Cailloux105 = Cailloux(880,720)
shop_magie_Cailloux106 = Cailloux(930,720)
shop_magie_Cailloux107 = Cailloux(950,180)
shop_magie_Cailloux108 = Cailloux(950,240)
shop_magie_Cailloux109 = Cailloux(950,300)
shop_magie_Cailloux110 = Cailloux(950,360)
shop_magie_Cailloux111 = Cailloux(950,420)
shop_magie_Cailloux112 = Cailloux(950,480)
shop_magie_Cailloux113 = Cailloux(950,540)
shop_magie_Cailloux114 = Cailloux(950,600)
shop_magie_Cailloux115 = Cailloux(950,660)
shop_magie_Cailloux116 = Cailloux(950,720)
shop_magie_Cailloux117 = Cailloux(236,340)
shop_magie_Cailloux118 = Cailloux(236,376)
shop_magie_Cailloux119 = Cailloux(720,340)
shop_magie_Cailloux120 = Cailloux(720,376)
shop_magie_Cailloux121 = Cailloux(405,373)
shop_magie_Cailloux122 = Cailloux(455,373)
shop_magie_Cailloux123 = Cailloux(505,373)
shop_magie_Cailloux124 = Cailloux(555,373)
shop_magie_Cailloux125 = Cailloux(480,245)

Glace2_Cailloux1 = Cailloux(815,197)
Glace2_Cailloux2 = Cailloux(815,232)
Glace2_Cailloux3 = Cailloux(190,486)
Glace2_Cailloux4 = Cailloux(190,516)
Glace2_Cailloux5 = Cailloux(863,868)
Glace2_Cailloux6 = Cailloux(863,904)
Glace2_Cailloux7 = Cailloux(94,819)
Glace2_Cailloux8 = Cailloux(94,854)

Boss_salle1 = Cailloux(257, 223)
Boss_salle2 = Cailloux(269, 223)
Boss_salle3 = Cailloux(257, 244)
Boss_salle4 = Cailloux(269, 244)

Boss_salle5 = Cailloux(478, 223)
Boss_salle6 = Cailloux(490, 223)
Boss_salle7 = Cailloux(478, 244)
Boss_salle8 = Cailloux(490, 244)

Boss_salle9 = Cailloux(257, 415)
Boss_salle10 = Cailloux(269, 415)
Boss_salle11 = Cailloux(257, 436)
Boss_salle12 = Cailloux(269, 436)

Boss_salle13 = Cailloux(478, 415)
Boss_salle14 = Cailloux(490, 415)
Boss_salle15 = Cailloux(478, 436)
Boss_salle16 = Cailloux(490, 436)

# Position de la fenêtre
J_x_decor_Base = 0
J_y_decor_Base = 0

Pnj_List_Base = [Megumin]

Mob_List_Base = []

Item_List_Base = []

Hitbox_Base = [ville_pub1, ville_pub2, ville_pub3, ville_pub4 , ville_pub5 , ville_pub6 , ville_guilde1 , ville_guilde2 , ville_guilde3 , ville_guilde4 , ville_guilde5 , ville_guilde6 , ville_guilde7 , ville_guilde8 , ville_guilde9 , ville_guilde10 , ville_shop1 , ville_shop2 , ville_shop3 , ville_shop4 , ville_shop5 , ville_shop6 , ville_shop7 , ville_shop8 , ville_shop9 , ville_shop10 , ville_shop11 , ville_shop12 , ville_shop13 , ville_shop14 , ville_maison1 , ville_maison2 , ville_maison3 , ville_maison4 , ville_maison5 , ville_maison6 , ville_maison7 , ville_maison8 , ville_maison9 , ville_maison10 , ville_maison11 , ville_maison12 , ville_eau1 , ville_eau2]

Sortie_Liste_Base = []

Marchand_Liste_Base = []

Map_Base = Salle(Pnj_List_Base, Mob_List_Base, Item_List_Base, Map_Base_Image, J_x_decor_Base, J_y_decor_Base, Hitbox_Base, Sortie_Liste_Base, Marchand_Liste_Base)

# Création salle dde glace
Pnj_List_Glace = []

Mob_List_Glace = []

Item_List_Glace = []

Hitbox_Glace = [Glace_Cailloux1, Glace_Cailloux2, Glace_Cailloux3, Glace_Cailloux4, Glace_Cailloux5, Glace_Cailloux6, Glace_Cailloux7, Glace_Cailloux8, Glace_Cailloux9, Glace_Cailloux10, Glace_Cailloux11, Glace_Cailloux12, Glace_Cailloux13, Glace_Cailloux14, Glace_Cailloux15, Glace_Cailloux16, Glace_Cailloux17, Glace_Cailloux18, Glace_Cailloux19, Glace_Cailloux20, Glace_Cailloux21, Glace_Cailloux22, Glace_Cailloux23, Glace_Cailloux24, Glace_Cailloux25, Glace_Cailloux26, Glace_Cailloux27, Glace_Cailloux28, Glace_Cailloux29, Glace_Cailloux30, Glace_Cailloux31, Glace_Cailloux32, Glace_Cailloux33, Glace_Cailloux34, Glace_Cailloux35, Glace_Cailloux36, Glace_Cailloux37, Glace_Cailloux38, Glace_Cailloux39, Glace_Cailloux40]

J_x_decor_Glace = 0
J_y_decor_Glace = 0

Sortie_Liste_Glace = []

Marchand_Liste_Glace = []

Map_Glace = Salle(Pnj_List_Glace, Mob_List_Glace, Item_List_Glace, Map_Glace_Image, J_x_decor_Glace, J_y_decor_Glace, Hitbox_Glace, Sortie_Liste_Glace, Marchand_Liste_Glace)

# Création Shop Classique
Pnj_List_Shop = []
Mob_List_Shop = []
Item_List_Shop = []
Hitbox_Shop1 = [ville_cite1, ville_cite2 , ville_cite3 , ville_cite4 , ville_cite5 , ville_cite6 , ville_cite7 , ville_cite8 , ville_cite9 , ville_cite10 , ville_cite11 , ville_cite12 , ville_cite13 , ville_cite14 , ville_cite15 , ville_cite16 , ville_cite17 , ville_cite18 , ville_cite19 , ville_cite20 , ville_cite21 , ville_cite22 , ville_cite23 , ville_cite24 , ville_cite25 , ville_cite26 , ville_cite27 , ville_cite28 , ville_cite29 , ville_cite30 , ville_cite31 , ville_cite32 , ville_cite33 , ville_cite34 , ville_cite35 , ville_cite36 , ville_cite37 , ville_cite38 , ville_cite39 , ville_cite40 , ville_cite41 , ville_cite42 , ville_cite43 , ville_cite44 , ville_cite45 , ville_cite46 , ville_cite48 , ville_cite49 , ville_cite50 , ville_cite51 , ville_cite52 , ville_cite53 , ville_cite54 , ville_cite55, ville_cite56]
SortieShop1 = []
Marchand_Shop1 = [Marchand_Arme]

Shop_Map = Salle(Pnj_List_Shop, Mob_List_Shop, Item_List_Shop, Shop1_Image, 0, 0, Hitbox_Shop1, SortieShop1, Marchand_Shop1)

# Création Shop Magie

SortieShop2 = []
Hitbox_Shop2 = [shop_magie_Cailloux1, shop_magie_Cailloux2, shop_magie_Cailloux3,shop_magie_Cailloux4,shop_magie_Cailloux5,shop_magie_Cailloux6,shop_magie_Cailloux7,shop_magie_Cailloux8,shop_magie_Cailloux9,shop_magie_Cailloux10,shop_magie_Cailloux11,shop_magie_Cailloux12,shop_magie_Cailloux13,shop_magie_Cailloux14,shop_magie_Cailloux15,shop_magie_Cailloux16,shop_magie_Cailloux17,shop_magie_Cailloux18,shop_magie_Cailloux19,shop_magie_Cailloux20,shop_magie_Cailloux21,shop_magie_Cailloux22,shop_magie_Cailloux23,shop_magie_Cailloux24,shop_magie_Cailloux25,shop_magie_Cailloux26,shop_magie_Cailloux27,shop_magie_Cailloux28,shop_magie_Cailloux29,shop_magie_Cailloux30,shop_magie_Cailloux31,shop_magie_Cailloux32,shop_magie_Cailloux33,shop_magie_Cailloux34,shop_magie_Cailloux35,shop_magie_Cailloux36,shop_magie_Cailloux37,shop_magie_Cailloux38,shop_magie_Cailloux39,shop_magie_Cailloux40,shop_magie_Cailloux41,shop_magie_Cailloux42,shop_magie_Cailloux43,shop_magie_Cailloux44,shop_magie_Cailloux45,shop_magie_Cailloux46,shop_magie_Cailloux47,shop_magie_Cailloux48,shop_magie_Cailloux49,shop_magie_Cailloux50,shop_magie_Cailloux51,shop_magie_Cailloux52,shop_magie_Cailloux53,shop_magie_Cailloux54,shop_magie_Cailloux55,shop_magie_Cailloux56,shop_magie_Cailloux57,shop_magie_Cailloux58,shop_magie_Cailloux59,shop_magie_Cailloux60,shop_magie_Cailloux61,shop_magie_Cailloux62,shop_magie_Cailloux63,shop_magie_Cailloux64,shop_magie_Cailloux65,shop_magie_Cailloux66,shop_magie_Cailloux67,shop_magie_Cailloux68,shop_magie_Cailloux69,shop_magie_Cailloux70,shop_magie_Cailloux71,shop_magie_Cailloux72,shop_magie_Cailloux73,shop_magie_Cailloux74,shop_magie_Cailloux75,shop_magie_Cailloux76,shop_magie_Cailloux77,shop_magie_Cailloux78,shop_magie_Cailloux79,shop_magie_Cailloux80,shop_magie_Cailloux81,shop_magie_Cailloux82,shop_magie_Cailloux83,shop_magie_Cailloux84,shop_magie_Cailloux85,shop_magie_Cailloux86,shop_magie_Cailloux87,shop_magie_Cailloux88,shop_magie_Cailloux89,shop_magie_Cailloux90,shop_magie_Cailloux91,shop_magie_Cailloux92,shop_magie_Cailloux93,shop_magie_Cailloux94,shop_magie_Cailloux95,shop_magie_Cailloux96,shop_magie_Cailloux97,shop_magie_Cailloux98,shop_magie_Cailloux99,shop_magie_Cailloux100,shop_magie_Cailloux101,shop_magie_Cailloux102,shop_magie_Cailloux103,shop_magie_Cailloux104,shop_magie_Cailloux105,shop_magie_Cailloux106,shop_magie_Cailloux107,shop_magie_Cailloux108,shop_magie_Cailloux109,shop_magie_Cailloux110,shop_magie_Cailloux111,shop_magie_Cailloux112,shop_magie_Cailloux113,shop_magie_Cailloux114,shop_magie_Cailloux115,shop_magie_Cailloux116,shop_magie_Cailloux117,shop_magie_Cailloux118,shop_magie_Cailloux119,shop_magie_Cailloux120,shop_magie_Cailloux121,shop_magie_Cailloux122,shop_magie_Cailloux123,shop_magie_Cailloux124,shop_magie_Cailloux125]
Marchand_Shop2 = [Marchand_Magie]

Shop2_Map = Salle(Pnj_List_Shop, Mob_List_Shop, Item_List_Shop, Shop2_Image, 0, 0, Hitbox_Shop2, SortieShop2, Marchand_Shop2)

# Création Plaine et Glace 2

Mob_Liste1 = [Mob_5, Mob_6, Mob_7, Mob_8]
Mob_Liste2 = [Mob_1, Mob_2, Mob_3, Mob_4]
Plaine_Hitbox = []
Glace_Hitbox = [Glace2_Cailloux1, Glace2_Cailloux2, Glace2_Cailloux3, Glace2_Cailloux4, Glace2_Cailloux4, Glace2_Cailloux5, Glace2_Cailloux6, Glace2_Cailloux7, Glace2_Cailloux8]
Sortieoui = []
Sortieoui2 = []
MarchandList = []

Glace2_Map = Salle(Pnj_List_Shop, Mob_Liste1, Item_List_Shop, Glace2_Image, 450, 0, Glace_Hitbox, Sortieoui, MarchandList)
Plaine_Map = Salle(Pnj_List_Shop, Mob_Liste2, Item_List_Shop, Plaine_Image, 450, 0, Plaine_Hitbox, Sortieoui2, MarchandList)

# Création Boss

Mob_Liste_Boss = [Boss_mob]
Boss_Hitbox = [Boss_salle1, Boss_salle2, Boss_salle3, Boss_salle4, Boss_salle5, Boss_salle6, Boss_salle7, Boss_salle8, Boss_salle9, Boss_salle10, Boss_salle11, Boss_salle12, Boss_salle13, Boss_salle14, Boss_salle15, Boss_salle16]
Sortieoui3 = []
MarchandList = []
Map_Boss = Salle(Pnj_List_Shop, Mob_Liste_Boss, Item_List_Shop, Boss_Image, 450, 0, Boss_Hitbox, Sortieoui3, MarchandList)


# Déclaration des sorties
Sortie_Glace2_Glace = ChangeSalle(500, 0, "paillasson.png", Map_Glace, 220, 150, 265, 527)
Sortie_Glace_Glace2 = ChangeSalle(470, 728, "paillasson.png", Glace2_Map, 250, 0, 275, 34)
Sortie_Glace_Boss = ChangeSalle(470, 0, "paillasson.png", Map_Boss, 100, 200, 280, 550)
Sortie_Glace2_Base = ChangeSalle(500, 1170, "paillasson.png", Map_Base, 235, 0, 325, 40)
Sortie_Base_Glace2 = ChangeSalle(560, 0, "paillasson.png", Glace2_Map, 250, 600, 271, 519)
Sortie_Base_Plaine = ChangeSalle(977, 340, "paillassonverticale.png", Plaine_Map, 0, 301, 34, 280)
Sortie_Plaine_Base = ChangeSalle(0, 566, "paillassonverticale.png", Map_Base, 400, 14, 533, 346)
Sortie_Base_Shop1 = ChangeSalle(690, 310, "paillasson_petit.png", Shop_Map, 50, 0, 290, 540)
Sortie_Base_Shop2 = ChangeSalle(305, 503, "paillasson_petit.png", Shop2_Map, 250, 150, 250, 550)
Sortie_Shop1_Base = ChangeSalle(320, 670, "paillasson.png", Map_Base, 300, 0, 390, 335)
Sortie_Shop2_Base = ChangeSalle(475, 834, "paillasson.png", Map_Base, 0, 0, 305, 526)


# On met les sorties dans chaque Salle
Map_Base.a_Sortie_Liste.append(Sortie_Base_Glace2)
Map_Base.a_Sortie_Liste.append(Sortie_Base_Shop1)
Map_Base.a_Sortie_Liste.append(Sortie_Base_Shop2)
Map_Base.a_Sortie_Liste.append(Sortie_Base_Plaine)
Glace2_Map.a_Sortie_Liste.append(Sortie_Glace2_Glace)
Glace2_Map.a_Sortie_Liste.append(Sortie_Glace2_Base)
Plaine_Map.a_Sortie_Liste.append(Sortie_Plaine_Base)
Map_Glace.a_Sortie_Liste.append(Sortie_Glace_Glace2)
Map_Glace.a_Sortie_Liste.append(Sortie_Glace_Boss)
Shop_Map.a_Sortie_Liste.append(Sortie_Shop1_Base)
Shop2_Map.a_Sortie_Liste.append(Sortie_Shop2_Base)

CurrentMap = Map_Base
Fond = CurrentMap.a_Image
screenWidth = 600
screenHeight = 600

Dialogue_x = 200
Dialogue_Y = 200

Perso_Hero = Hero(220, 310)   # Hero(screenWidth / 2 - 50, screenHeight / 2 - 50)

# Attribut pour savoir si on a ouvert un shop
AucunShop = 0
Shop_Arme = 1
Shop_Magie = 2
CurrentShop = 0

# Bouton pour augmenter les stats lors d'un lvl up

Bouton_image = pygame.image.load(os.path.join(assets, "Up.png"))
Bouton_image = pygame.transform.scale(Bouton_image, (50, 50))

Bouton_health = Button_lvl(Bouton_image, 50, 20)
Bouton_mana = Button_lvl(Bouton_image, 50, 120)
Bouton_strength = Button_lvl(Bouton_image, 50, 220)
Bouton_def = Button_lvl(Bouton_image, 50, 320)
Bouton_int = Button_lvl(Bouton_image, 50, 420)
Bouton_vitesse = Button_lvl(Bouton_image, 50, 520)

Bouton_lvl = [Bouton_health, Bouton_mana, Bouton_strength, Bouton_def, Bouton_int, Bouton_vitesse]

# Déclaration des etats :
Bas = 00
Gauche = 1
Haut = 2
Droite = 3

Attaque = 5
Idle = 6
Marche = 7

Homme = 10
Femme = 20


# Fonction pour verifier la hitbox


def inRects(perso):
    directionblock = [False, False, False, False]
    x = perso.aX
    y = perso.aY
    height, width = 33, 35
    for one_cailloux in CurrentMap.a_Tab_Hitbox:
        pixel1 = x + width, y
        pixel2 = x + width, y + height
        if one_cailloux.inRect(pixel1) or one_cailloux.inRect(pixel2):
            directionblock[0] = True
        pixel1 = x, y + height
        pixel2 = x + width, y + height
        if one_cailloux.inRect(pixel1) or one_cailloux.inRect(pixel2):
            directionblock[1] = True
        pixel1 = x, y
        pixel2 = x, y + height
        if one_cailloux.inRect(pixel1) or one_cailloux.inRect(pixel2):
            directionblock[2] = True
        pixel1 = x, y
        pixel2 = x + width, y
        if one_cailloux.inRect(pixel1) or one_cailloux.inRect(pixel2):
            directionblock[3] = True
    return directionblock


def inRectsVitesse(perso):
    directionblock = [False, False, False, False]
    x = perso.aX
    y = perso.aY
    vitesse = Perso_Hero.vitesse
    height, width = 33, 35
    for one_cailloux in CurrentMap.a_Tab_Hitbox:
        pixel1 = x + width + vitesse, y
        pixel2 = x + width + vitesse, y + height
        if one_cailloux.inRect(pixel1) or one_cailloux.inRect(pixel2):
            directionblock[0] = one_cailloux.aX
        pixel1 = x, y + height + vitesse
        pixel2 = x + width, y + height + vitesse
        if one_cailloux.inRect(pixel1) or one_cailloux.inRect(pixel2):
            directionblock[1] = one_cailloux.aY
        pixel1 = x - vitesse, y
        pixel2 = x - vitesse, y + height
        if one_cailloux.inRect(pixel1) or one_cailloux.inRect(pixel2):
            directionblock[2] = one_cailloux.aX + 50
        pixel1 = x, y - vitesse
        pixel2 = x + width, y - vitesse
        if one_cailloux.inRect(pixel1) or one_cailloux.inRect(pixel2):
            directionblock[3] = one_cailloux.aY + 60
    return directionblock

# Fonction pour équiper un item


def equipe(p_hero, p_item):
    if p_item.ckoi() == "Epee":
        p_hero.a_weapon = p_item
    elif p_item.ckoi() == "Bottes":
        p_hero.a_boot = p_item
    else:
        p_hero.a_armor = p_item
    Perso_Hero.actustat()

# Fonction pour verifier la glissade


def isSliding(perso):
    x = perso.aX + CurrentMap.a_XDecor
    y = perso.aY + CurrentMap.a_YDecor
    if CurrentMap != Map_Glace:
        # print("false")
        return False
    if (345 < x < 649 and 0 <= y < 180 ) or (294 < x < 716 and 640 < y < 760) or ( 52 < x < 100 and 692 < y < 761) or (897 < x < 950 and 692 < y < 761):
        # print("false")
        return False
    else:
        # print("true")
        return True


###################################################################################
# Initialize pygame

pygame.init()
play = 0


def playMusic(file, play):
    if (play != 1):
        pygame.mixer.music.stop()
        pygame.mixer.music.load(os.path.join(music, file))
        pygame.mixer.music.play(-1)


def playSound(file):
    pygame.mixer.Sound(os.path.join(sound, file)).play()


son_glisse = pygame.mixer.Sound(os.path.join(sound, "glissade.wav"))


def playGlissade():
    son_glisse.play()


def volume():
    pygame.mixer.Sound.set_volume(pygame.mixer.Sound(os.path.join(sound, "glissade.wav")), 1.0)


def stopGlissade(): #ne stoppe pas pour une raison obscure
    son_glisse.stop()

# set police for text
text_font = pygame.font.SysFont("arial", 50)
Gold_font = pygame.font.SysFont("arial", 20)
GG_Font = pygame.font.SysFont("arial", 50)

# Set the width and height of the screen [width,height]
screen = pygame.display.set_mode((800, 400))
# screen = pygame.display.set_mode((screenWidth, screenHeight))

# Set title of screen
pygame.display.set_caption("Elemental Quest")

# Loop until the user clicks the close button.
done = False
done2 = False
done3 = False
done4 = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

pygame.mouse.set_visible(1)
# Programme principal
while not done:

    while not done2:
        for event in pygame.event.get():  # User did something

            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
                done2 = True
                done3 = True
                done4 = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            done2 = True
            temps.sleep(0.3)
        screen.blit(Title_Screen, (0, 0))

        pygame.display.flip()

    while not done3:
        for event in pygame.event.get():  # User did something

            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
                done3 = True
                done4 = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            x = pos[0]
            if x<400:
                Perso_Hero.a_genre = Homme
            done3 = True
            temps.sleep(0.3)
        screen.blit(Selection_Screen, (0, 0))

        pygame.display.flip()

    while not done4:
        for event in pygame.event.get():  # User did something

            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
                done4 = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            x = pos[0]
            if 0 <= x < 266:
                Perso_Hero.a_color = 0
            elif 266 <= x < 532:
                Perso_Hero.a_color = 1
            elif 532 <= x:
                Perso_Hero.a_color = 2
            done4 = True
            Perso_Hero.updatesprite()
            temps.sleep(0.3)
            screen = pygame.display.set_mode((screenWidth, screenHeight))
        screen.blit(Couleur_Screen, (0, 0))

        pygame.display.flip()

    event = pygame.event.Event(pygame.USEREVENT)

    for event in pygame.event.get():  # User did something

        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    KeysPressed = pygame.key.get_pressed()

    time = int(pygame.time.get_ticks() / 100)

    # musique
    if (CurrentMap == Map_Base):
        playMusic("Town1.mp3", play)
        play = 1
    if (CurrentMap == Shop_Map):
        playMusic("Shop2.mp3", play)
        play = 1
    if (CurrentMap == Shop2_Map):
        playMusic("Shop1.mp3", play)
        play = 1
    if (CurrentMap == Plaine_Map):
        playMusic("Plains1.mp3", play)
        play = 1
    if (CurrentMap == Map_Glace):
        playMusic("Ice Path.mp3", play)
        play = 1
    if (CurrentMap == Glace2_Map):
        playMusic("BattleMusic3.mp3", play)
        play = 1
    if (CurrentMap == Map_Boss):
        playMusic("BattleMusic5.mp3", play)
        play = 1

    # Déplacement du Hero si il n'est pas entrain de faire une autre action
    if Perso_Hero.a_Duree == 0:

        if not KeysPressed[pygame.K_UP] and not KeysPressed[pygame.K_DOWN] and not KeysPressed[pygame.K_RIGHT] and not KeysPressed[pygame.K_LEFT]:
            Perso_Hero.a_Etat = Idle

        collision = inRects(Perso_Hero)
        collision_vitesse = inRectsVitesse(Perso_Hero)

        # if ne glisse pas, alors on gère toutes les directions

        if Perso_Hero.a_etat == "marche":
            stopGlissade()
            if KeysPressed[pygame.K_UP] and collision[3] is False:
                Perso_Hero.a_Etat = Marche
                Perso_Hero.a_dir = Haut
                if isSliding(Perso_Hero) is True and CurrentMap == Map_Glace:
                    Perso_Hero.a_etat = "slide_up"
                    volume()
                    playGlissade()
                if collision_vitesse[3] is not False:
                    Perso_Hero.aY = collision_vitesse[3] - CurrentMap.a_YDecor + 1
                else:
                    if Perso_Hero.aY > screenHeight / 2 - 25:
                        Perso_Hero.aY -= Perso_Hero.vitesse
                        if Perso_Hero.aY < screenHeight / 2 - 25:
                            Perso_Hero.aY = screenHeight / 2 - 25
                    else:
                        CurrentMap.a_YDecor -= Perso_Hero.vitesse
                        if CurrentMap.a_YDecor < 0:
                            CurrentMap.a_YDecor = 0
                            Perso_Hero.aY -= Perso_Hero.vitesse

            if KeysPressed[pygame.K_DOWN] and collision[1] is False:
                Perso_Hero.a_Etat = Marche
                Perso_Hero.a_dir = Bas
                if isSliding(Perso_Hero) is True and CurrentMap == Map_Glace:
                    Perso_Hero.a_etat = "slide_down"
                    volume()
                    playGlissade()
                if collision_vitesse[1] is not False:
                    Perso_Hero.aY = collision_vitesse[1] - 33 - CurrentMap.a_YDecor - 1
                else:
                    if Perso_Hero.aY < screenHeight / 2 - 25:
                        Perso_Hero.aY += Perso_Hero.vitesse
                        if Perso_Hero.aY > screenHeight / 2 - 25:
                            Perso_Hero.aY = screenHeight / 2 - 25
                    else:
                        CurrentMap.a_YDecor += Perso_Hero.vitesse
                        if CurrentMap.a_YDecor + screenHeight > Fond.get_height():
                            CurrentMap.a_YDecor = Fond.get_height() - screenHeight
                            Perso_Hero.aY += Perso_Hero.vitesse

            if KeysPressed[pygame.K_LEFT] and collision[2] is False:
                Perso_Hero.a_Etat = Marche
                Perso_Hero.a_dir = Gauche
                if isSliding(Perso_Hero) is True and CurrentMap == Map_Glace:
                    Perso_Hero.a_etat = "slide_left"
                    volume()
                    playGlissade()
                if collision_vitesse[2] is not False:
                    Perso_Hero.aX = collision_vitesse[2] - CurrentMap.a_XDecor + 1
                else:
                    if Perso_Hero.aX > screenWidth / 2 - 25:
                        Perso_Hero.aX -= Perso_Hero.vitesse
                        if Perso_Hero.aX < screenWidth / 2 - 25:
                            Perso_Hero.aX = screenWidth / 2 - 25
                    else:
                        CurrentMap.a_XDecor -= Perso_Hero.vitesse
                        if CurrentMap.a_XDecor < 0:
                            CurrentMap.a_XDecor = 0
                            Perso_Hero.aX -= Perso_Hero.vitesse

            if KeysPressed[pygame.K_RIGHT] and collision[0] is False:
                Perso_Hero.a_Etat = Marche
                Perso_Hero.a_dir = Droite
                if isSliding(Perso_Hero) is True and CurrentMap == Map_Glace:
                    Perso_Hero.a_etat = "slide_right"
                    volume()
                    playGlissade()
                if collision_vitesse[0] is not False:
                    Perso_Hero.aX = collision_vitesse[0] - 35 - CurrentMap.a_XDecor - 1
                else:
                    if Perso_Hero.aX < screenWidth / 2 - 25:
                        Perso_Hero.aX += Perso_Hero.vitesse
                        if Perso_Hero.aX > screenWidth / 2 - 25:
                            Perso_Hero.aX = screenWidth / 2 - 25
                    else:
                        CurrentMap.a_XDecor += Perso_Hero.vitesse
                        if CurrentMap.a_XDecor + screenWidth > Fond.get_width():
                            CurrentMap.a_XDecor = Fond.get_width() - screenWidth
                            Perso_Hero.aX += Perso_Hero.vitesse
        elif Perso_Hero.a_etat == "slide_up":
            if collision_vitesse[3] is not False:
                Perso_Hero.aY = collision_vitesse[3] - CurrentMap.a_YDecor + 1
                Perso_Hero.a_etat = "marche"
                stopGlissade()
            elif not isSliding(Perso_Hero):
                Perso_Hero.a_etat = "marche"
                stopGlissade()
            else:
                if Perso_Hero.aY > screenHeight / 2 - 25:
                    Perso_Hero.aY -= Perso_Hero.vitesse
                    if Perso_Hero.aY < screenHeight / 2 - 25:
                        Perso_Hero.aY = screenHeight / 2 - 25
                else:
                    CurrentMap.a_YDecor -= Perso_Hero.vitesse
                    if CurrentMap.a_YDecor < 0:
                        CurrentMap.a_YDecor = 0
                        Perso_Hero.aY -= Perso_Hero.vitesse

        elif Perso_Hero.a_etat == "slide_down":
            if collision_vitesse[1] is not False:
                Perso_Hero.aY = collision_vitesse[1] - 33 - CurrentMap.a_YDecor - 1
                Perso_Hero.a_etat = "marche"
                stopGlissade()
            elif not isSliding(Perso_Hero):
                Perso_Hero.a_etat = "marche"
                stopGlissade()
            else:
                if Perso_Hero.aY < screenHeight / 2 - 25:
                    Perso_Hero.aY += Perso_Hero.vitesse
                    if Perso_Hero.aY > screenHeight / 2 - 25:
                        Perso_Hero.aY = screenHeight / 2 - 25
                else:
                    CurrentMap.a_YDecor += Perso_Hero.vitesse
                    if CurrentMap.a_YDecor + screenHeight > Fond.get_height():
                        CurrentMap.a_YDecor = Fond.get_height() - screenHeight
                        Perso_Hero.aY += Perso_Hero.vitesse

        elif Perso_Hero.a_etat == "slide_left":
            if collision_vitesse[2] is not False:
                Perso_Hero.aX = collision_vitesse[2] - CurrentMap.a_XDecor + 1
                Perso_Hero.a_etat = "marche"
                stopGlissade()
            elif not isSliding(Perso_Hero):
                Perso_Hero.a_etat = "marche"
                stopGlissade()
            else:
                if Perso_Hero.aX > screenWidth / 2 - 25:
                    Perso_Hero.aX -= Perso_Hero.vitesse
                    if Perso_Hero.aX < screenWidth / 2 - 25:
                        Perso_Hero.aX = screenWidth / 2 - 25
                else:
                    CurrentMap.a_XDecor -= Perso_Hero.vitesse
                    if CurrentMap.a_XDecor < 0:
                        CurrentMap.a_XDecor = 0
                        Perso_Hero.aX -= Perso_Hero.vitesse

        elif Perso_Hero.a_etat == "slide_right":
            if collision_vitesse[0] is not False:
                Perso_Hero.aX = collision_vitesse[0] - 35 - CurrentMap.a_XDecor - 1
                Perso_Hero.a_etat = "marche"
                stopGlissade()
            elif not isSliding(Perso_Hero):
                Perso_Hero.a_etat = "marche"
                stopGlissade()
            else:
                if Perso_Hero.aX < screenWidth / 2 - 25:
                    Perso_Hero.aX += Perso_Hero.vitesse
                    if Perso_Hero.aX > screenWidth / 2 - 25:
                        Perso_Hero.aX = screenWidth / 2 - 25
                else:
                    CurrentMap.a_XDecor += Perso_Hero.vitesse
                    if CurrentMap.a_XDecor + screenWidth > Fond.get_width():
                        CurrentMap.a_XDecor = Fond.get_width() - screenWidth
                        Perso_Hero.aX += Perso_Hero.vitesse

        else:
            print("oui")

        # Sinon, alors on bouge dans la direction retenue pendant la glissade
        # On check les collisions
        # Si collision, on arrête l'état glissade

    else:
        Perso_Hero.a_Duree -= 1

# Pour éviter que le Perso sorte de l'écran
    if Perso_Hero.aX < 0:
        Perso_Hero.aX = 0
        Perso_Hero.a_etat = "marche"
        stopGlissade()
    if Perso_Hero.aY < 0:
        Perso_Hero.aY = 0
        Perso_Hero.a_etat = "marche"
        stopGlissade()
    if Perso_Hero.aX + 35 > screenWidth:
        Perso_Hero.aX = screenWidth - 35
        Perso_Hero.a_etat = "marche"
        stopGlissade()
    if Perso_Hero.aY + 33 > screenHeight:
        Perso_Hero.aY = screenHeight - 33
        Perso_Hero.a_etat = "marche"
        stopGlissade()
    hero_hitbox = (Perso_Hero.aX, Perso_Hero.aY, 33, 35)

# Affiche les hitbox des cailloux
    for onecailloux in CurrentMap.a_Tab_Hitbox:
        onecailloux.affiche_aX = onecailloux.aX - CurrentMap.a_XDecor
        onecailloux.affiche_aY = onecailloux.aY - CurrentMap.a_YDecor
        pygame.draw.rect(screen, (255, 0, 0), (onecailloux.affiche_aX, onecailloux.affiche_aY, 50, 60), 2)

# Test si le joueurs se trouve près d'un marchand pour ouvrir le shop
    for one_marchant in CurrentMap.a_Marchand_Liste:
        QuelMarchand = Perso_Hero.ismarchand(one_marchant, CurrentMap .a_XDecor, CurrentMap.a_YDecor)
        if QuelMarchand == "MarchandArme":
            CurrentShop = Shop_Arme
            break
        if QuelMarchand == "MarchandMagie":
            CurrentShop = Shop_Magie
            break
        else:
            CurrentShop = AucunShop

# Affichage du shop actuel
    if CurrentShop == Shop_Arme:
        if event.type == pygame.MOUSEBUTTONDOWN:
            # print("Achat arme")
            pos = pygame.mouse.get_pos()
            y = pos[1]
            if 10 <= y <= 193:
                if Shop_Arme_Base.a_Item1 is not None:
                    if Perso_Hero.a_gold >= Shop_Arme_Base.a_Item1.a_Prix:
                        Perso_Hero.a_gold -= Shop_Arme_Base.a_Item1.a_Prix
                        equipe(Perso_Hero, Shop_Arme_Base.a_Item1)
                        Shop_Arme_Base.a_Item1 = None
            elif 193 <= y <= 193*2:
                if Shop_Arme_Base.a_Item2 is not None:
                    if Perso_Hero.a_gold >= Shop_Arme_Base.a_Item2.a_Prix:
                        Perso_Hero.a_gold -= Shop_Arme_Base.a_Item2.a_Prix
                        equipe(Perso_Hero, Shop_Arme_Base.a_Item2)
                        Shop_Arme_Base.a_Item2 = None
            elif 193*2 <= y <= 193*3:
                if Shop_Arme_Base.a_Item3 is not None:
                    if Perso_Hero.a_gold >= Shop_Arme_Base.a_Item3.a_Prix:
                        Perso_Hero.a_gold -= Shop_Arme_Base.a_Item3.a_Prix
                        equipe(Perso_Hero, Shop_Arme_Base.a_Item3)
                        Shop_Arme_Base.a_Item3 = None
    elif CurrentShop == Shop_Magie:
        if event.type == pygame.MOUSEBUTTONDOWN:
            # print("Achat magie")
            pos = pygame.mouse.get_pos()
            y = pos[1]
            if 10 <= y <= 193:
                if Shop_Magie_Base.a_Item1 is not None:
                    if Perso_Hero.a_gold >= Shop_Magie_Base.a_Item1.a_Prix:
                        Perso_Hero.a_gold -= Shop_Magie_Base.a_Item1.a_Prix
                        equipe(Perso_Hero, Shop_Magie_Base.a_Item1)
                        Shop_Magie_Base.a_Item1 = None
            elif 193 <= y <= 193*2:
                if Shop_Magie_Base.a_Item2 is not None:
                    if Perso_Hero.a_gold >= Shop_Magie_Base.a_Item2.a_Prix:
                        Perso_Hero.a_gold -= Shop_Magie_Base.a_Item2.a_Prix
                        equipe(Perso_Hero, Shop_Magie_Base.a_Item2)
                        Shop_Magie_Base.a_Item2 = None
            elif 193*2 <= y <= 193*3:
                if Shop_Magie_Base.a_Item3 is not None:
                    if Perso_Hero.a_gold >= Shop_Magie_Base.a_Item3.a_Prix:
                        Perso_Hero.a_gold -= Shop_Magie_Base.a_Item3.a_Prix
                        equipe(Perso_Hero, Shop_Magie_Base.a_Item3)
                        Shop_Magie_Base.a_Item3 = None
    else:
        # Test si clic gauche, si oui met le sprite attaque et test si un mob est proche
        if event.type == pygame.MOUSEBUTTONDOWN and Perso_Hero.a_Duree == 0:
            Perso_Hero.attaque()
            playSound("epeejoueur2.wav")
            for one_Mob in CurrentMap.a_Mob_List:
                one_Mob.getattack(Perso_Hero, CurrentMap.a_XDecor, CurrentMap.a_YDecor)
                playSound("attaqueennemi2.wav")

# Test si le perso est proche de la sortie, si oui le change de salle
    for one_Sortie in CurrentMap.a_Sortie_Liste:
        if Perso_Hero.aX + 35 > one_Sortie.aX - CurrentMap.a_XDecor and Perso_Hero.aX < one_Sortie.aX + one_Sortie.a_Image.get_width() - CurrentMap.a_XDecor and Perso_Hero.aY + 33 > one_Sortie.aY - CurrentMap.a_YDecor and Perso_Hero.aY < one_Sortie.aY + one_Sortie.a_Image.get_height() - CurrentMap.a_YDecor:
            CurrentMap = one_Sortie.a_Salle
            Fond = CurrentMap.a_Image
            CurrentMap.a_XDecor = one_Sortie.aX_Decor
            CurrentMap.a_YDecor = one_Sortie.aY_Decor
            Perso_Hero.aX = one_Sortie.aX_Perso
            Perso_Hero.aY = one_Sortie.aY_Perso
            play = 0

# Fond + caméra
    ZoneCam = pygame.Rect(CurrentMap.a_XDecor, CurrentMap.a_YDecor, screenWidth, screenHeight)
    screen.blit(Fond, (0, 0), area=ZoneCam)

# Affiche le perso
    screen.blit(Perso_Hero.quelimage(time), (Perso_Hero.aX, Perso_Hero.aY))

    # pygame.draw.rect(screen, (255, 0, 0), hero_hitbox, 2)
    # pygame.draw.rect(screen, (255, 0, 255), (Perso_Hero.aX - Perso_Hero.vitesse, Perso_Hero.aY - Perso_Hero.vitesse, 33 + 2*Perso_Hero.vitesse, 35 + 2*Perso_Hero.vitesse), 2)

    if Perso_Hero.a_health <= 0:
        Perso_Hero.a_health = 100
        CurrentMap = Map_Base
        CurrentMap.a_XDecor = 250
        CurrentMap.a_XDecor = 100
        Perso_Hero.aX = 250
        Perso_Hero.aY = 315
        Fond = CurrentMap.a_Image
        play = 0

# Affichage de chaque pnj / Mob et Sortie de la pièce courante
    for one_Pnj in CurrentMap.a_Pnj_List:
        screen.blit(one_Pnj.mouv(time), (one_Pnj.aX - CurrentMap.a_XDecor, one_Pnj.aY - CurrentMap.a_YDecor))

    for one_Mob in CurrentMap.a_Mob_List:
        if one_Mob.a_health > 0:
            one_Mob.move(Perso_Hero.aX + CurrentMap.a_XDecor, Perso_Hero.aY + CurrentMap.a_YDecor)
            one_Mob.attaque(Perso_Hero, CurrentMap.a_XDecor, CurrentMap.a_YDecor)
            screen.blit(one_Mob.imagequel(time), (one_Mob.aX - CurrentMap.a_XDecor, one_Mob.aY - CurrentMap.a_YDecor))
        else:
            Perso_Hero.a_exp += one_Mob.xp
            Perso_Hero.a_gold += one_Mob.gold
            playSound("mortennemi2.wav")
            if one_Mob == Boss_mob:
                GG_text = GG_Font.render("Bravo vous avez terminé ! ", True, [255, 0, 0])
                screen.blit(GG_text, (50, 200))
                pygame.display.flip()
                temps.sleep(5)
                play = 0
                pygame.quit()
            CurrentMap.a_Mob_List.remove(one_Mob)
    #for one_Sortie in CurrentMap.a_Sortie_Liste:
       # screen.blit(one_Sortie.a_Image, (one_Sortie.aX - CurrentMap.a_XDecor, one_Sortie.aY - CurrentMap.a_YDecor))
    for one_marchant in CurrentMap.a_Marchand_Liste:
        screen.blit(one_marchant.image(time), (one_marchant.aX - CurrentMap.a_XDecor, one_marchant.aY - CurrentMap.a_YDecor))
        # Affichage du shop actuel
        if CurrentShop == Shop_Arme:
            pygame.draw.rect(screen, [0, 0, 0], [10, 10, 580, 580])
            pygame.draw.line(screen, [255, 255, 255], (10, 193), (589, 193))
            pygame.draw.line(screen, [255, 255, 255], (10, 193*2), (589, 193*2))
            Marchand_Arme.aShop.dessine(screen)

        elif CurrentShop == Shop_Magie:
            pygame.draw.rect(screen, [0, 0, 0], [10, 10, 580, 580])
            pygame.draw.rect(screen, [0, 0, 0], [10, 10, 580, 580])
            pygame.draw.line(screen, [255, 255, 255], (10, 193), (589, 193))
            pygame.draw.line(screen, [255, 255, 255], (10, 193 * 2), (589, 193 * 2))
            Marchand_Magie.aShop.dessine(screen)

    #for onecailloux in CurrentMap.a_Tab_Hitbox:
     #   pygame.draw.rect(screen, (255, 0, 0), (onecailloux.affiche_aX, onecailloux.affiche_aY, 50, 60), 2)

    if Perso_Hero.actulvl():
        done_lvl = False
        points_lvl = 3
        while not done_lvl:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # If user clicked close
                    done_lvl = True
                    done = True  # Flag that we are done so we exit this loop
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    x = pos[0]
                    y = pos[1]
                    numero = 0
                    for one_button in Bouton_lvl:
                        numero += 1
                        if one_button.appuie(x, y):
                            points_lvl -= 1
                            if numero == 1:
                                Perso_Hero.a_max_health += 10
                                Perso_Hero.a_health += 10
                            elif numero == 2:
                                Perso_Hero.a_mana += 10
                            elif numero == 3:
                                Perso_Hero.a_strength += 5
                            elif numero == 4:
                                Perso_Hero.a_def += 5
                            elif numero == 5:
                                Perso_Hero.a_int += 5
                            elif numero == 6:
                                Perso_Hero.vitesse += 1

            pygame.draw.rect(screen, [146, 76, 61], [10, 10, 580, 580])
            for one_button in Bouton_lvl:
                screen.blit(one_button.a_image, (one_button.a_x, one_button.a_y))
            text = Gold_font.render("Points de compétence restant : " + str(points_lvl), True, [255, 255, 255])
            screen.blit(text, (300, 5))
            text = Gold_font.render(" Augmente ta santé max de 10", True, [255, 255, 255])
            screen.blit(text, (110, 30))
            text = Gold_font.render(" Augmente ton mana max de 10 (inutile) ", True, [255, 255, 255])
            screen.blit(text, (110, 130))
            text = Gold_font.render(" Augmente ta force de 5", True, [255, 255, 255])
            screen.blit(text, (110, 230))
            text = Gold_font.render("  Augmente ta defense de 5", True, [255, 255, 255])
            screen.blit(text, (110, 330))
            text = Gold_font.render(" Augmente ton intelligence de 5 (inutile)", True, [255, 255, 255])
            screen.blit(text, (110, 430))
            text = Gold_font.render(" Augmente ta vitesse de 1", True, [255, 255, 255])
            screen.blit(text, (110, 530))
            clock.tick(30)
            pygame.display.flip()
            if points_lvl <= 0:
                done_lvl = True

    lvl_text = Gold_font.render("Niveau : " + str(Perso_Hero.a_lvl), True, [255, 0, 0])
    screen.blit(lvl_text, (0, 21))
    exp_text = Gold_font.render("Expérience : " + str(Perso_Hero.a_exp), True, [255, 0, 0])
    screen.blit(exp_text, (0, 42))
    expn_text = Gold_font.render("Prochain niveau à : " + str(Perso_Hero.a_exp_lvl_need) + " points d'éxpérience", True, [255, 0, 0])
    screen.blit(expn_text, (0, 63))
    Health_text = Gold_font.render("Santé : " + str(Perso_Hero.a_health) + " / " + str(Perso_Hero.a_max_health), True, [255, 0, 0])
    screen.blit(Health_text, (0, 0))
    for one_marchant in CurrentMap.a_Marchand_Liste:
        # Affichage du shop actuel
        if CurrentShop == Shop_Arme:
            pygame.draw.rect(screen, [0, 0, 0], [10, 10, 580, 580])
            pygame.draw.line(screen, [255, 255, 255], (10, 193), (589, 193))
            pygame.draw.line(screen, [255, 255, 255], (10, 193*2), (589, 193*2))
            Marchand_Arme.aShop.dessine(screen)

        elif CurrentShop == Shop_Magie:
            pygame.draw.rect(screen, [0, 0, 0], [10, 10, 580, 580])
            pygame.draw.rect(screen, [0, 0, 0], [10, 10, 580, 580])
            pygame.draw.line(screen, [255, 255, 255], (10, 193), (589, 193))
            pygame.draw.line(screen, [255, 255, 255], (10, 193 * 2), (589, 193 * 2))
            Marchand_Magie.aShop.dessine(screen)
    gold_text = Gold_font.render("Gold : " + str(Perso_Hero.a_gold), True, [255, 0, 255])
    screen.blit(gold_text, (20, 565))

    # test pour chaque pnj si le joueur est assez proche pour afficher le dialogue
    for one_Pnj in CurrentMap.a_Pnj_List:
        zone_text = text_font.render(Perso_Hero.dialogue(one_Pnj, CurrentMap.a_XDecor, CurrentMap.a_YDecor), True, [255, 255, 0])
        screen.blit(zone_text, (0, 500))


    # 60 fps
    clock.tick(60)
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

pygame.quit()
