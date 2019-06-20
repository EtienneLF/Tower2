import inspect
import os
import pygame
from Class.Button import Button_lvl
from Class.Cailloux import Cailloux
from Class.Hero import Hero
from Class.Item import Epee, Bottes, Armure
from Class.Mob import Mob
from Class.Perso import Pnj, MarchandArme, MarchandMagie
from Class.Salle import Salle, ChangeSalle
from Class.Shop import Shop

# recherche du repertoire de travail bonjour

scriptPATH = os.path.abspath(inspect.getsourcefile(lambda: 0))  # compatible interactive Python Shell
scriptDIR = os.path.dirname(scriptPATH)
assets = os.path.join(scriptDIR, "data")

# Charge les images des différentes map
Map_Base_Image = pygame.image.load(os.path.join(assets, "Carte.jpg"))
Map_Glace_Image = pygame.image.load(os.path.join(assets, "Glace.PNG"))
Map_Lave_Image = pygame.image.load(os.path.join(assets, "Lave.PNG"))

# Création équipement
Excalibur = Epee("Excalibur", 1, 10, "C'est soit disant la meilleur épée du royaume")
Excalibur.a_Image = pygame.image.load(os.path.join(assets, "Epee.png"))
Excalibur.a_Image = pygame.transform.scale(Excalibur.a_Image, (100, 100))
Tee_shirt = Armure("Tee_shirt", 1, 10, "Au moins vos bourrelets ne se verront plus")
Tee_shirt.a_Image = pygame.image.load(os.path.join(assets, "Haut.png"))
Tee_shirt.a_Image = pygame.transform.scale(Tee_shirt.a_Image, (100, 100))
Sandales = Bottes("Bottes", 1, 5, "Au moins si vous marchez dans la boue tout ira bien")
Sandales.a_Image = pygame.image.load(os.path.join(assets, "Bottes.jpg"))
Sandales.a_Image = pygame.transform.scale(Sandales.a_Image, (100, 100))

# Création Shop
Shop_Arme_Base = Shop(Excalibur, Tee_shirt, Sandales)

Shop_Magie_Base = Shop(Sandales, Sandales, Excalibur)

# Création marchant
Marchand_Arme = MarchandArme(800, 800, "Marchand_Arme.png", Shop_Arme_Base)
Marchand_Arme.aImage = pygame.transform.scale(Marchand_Arme.aImage, (100, 160))

Marchand_Magie = MarchandMagie(800, 1000, "Marchand_Magie.png", Shop_Magie_Base)
Marchand_Magie.aImage = pygame.transform.scale(Marchand_Magie.aImage, (100, 160))
# Création salle de base
# Pnj
Megumin = Pnj(1125, 450, "Megumin.png", "Bonjour EXPLOSION", "Megumin")
Megumin.aImage = pygame.transform.scale(Megumin.aImage, (100, 160))

# Mob
Mob_1 = Mob(500, 500, 100, "Megumin.png", 5, 100, 10, 5)
Mob_1.aImage = pygame.transform.scale(Megumin.aImage, (100, 160))

Mob_2 = Mob(600, 500, 100, "Megumin.png", 5, 100, 10, 5)
Mob_2.aImage = pygame.transform.scale(Megumin.aImage, (100, 160))

Mob_3 = Mob(100, 100, 100, "Megumin.png", 5, 100, 10, 5)
Mob_3.aImage = pygame.transform.scale(Megumin.aImage, (100, 160))

# Création cailloux
Glace_Cailloux1 = Cailloux(303, 297)
Glace_Cailloux2 = Cailloux(417, 356)
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
Glace_Cailloux33 = Cailloux(241, 585)
Glace_Cailloux34 = Cailloux(241, 635)
Glace_Cailloux35 = Cailloux(705, 585)
Glace_Cailloux36 = Cailloux(705, 635)
Glace_Cailloux37 = Cailloux(180, 646)
Glace_Cailloux38 = Cailloux(180, 704)
Glace_Cailloux39 = Cailloux(768, 646)
Glace_Cailloux40 = Cailloux(768, 704)

# Position de la fenêtre
J_x_decor_Base = 0
J_y_decor_Base = 0

Pnj_List_Base = [Megumin]

Mob_List_Base = [Mob_1, Mob_2]

Item_List_Base = []

Hitbox_Base = []

Sortie_Liste_Base = []

Marchand_Liste_Base = [Marchand_Arme, Marchand_Magie]

Map_Base = Salle(Pnj_List_Base, Mob_List_Base, Item_List_Base, Map_Base_Image, J_x_decor_Base, J_y_decor_Base, Hitbox_Base, Sortie_Liste_Base, Marchand_Liste_Base)

# Création salle dde glace
Pnj_List_Glace = []

Mob_List_Glace = [Mob_3]

Item_List_Glace = []

Hitbox_Glace = [Glace_Cailloux1, Glace_Cailloux2, Glace_Cailloux3, Glace_Cailloux4, Glace_Cailloux5, Glace_Cailloux6, Glace_Cailloux7, Glace_Cailloux8, Glace_Cailloux9, Glace_Cailloux10, Glace_Cailloux11, Glace_Cailloux12, Glace_Cailloux13, Glace_Cailloux14, Glace_Cailloux15, Glace_Cailloux16, Glace_Cailloux17, Glace_Cailloux18, Glace_Cailloux19, Glace_Cailloux20, Glace_Cailloux21, Glace_Cailloux22, Glace_Cailloux23, Glace_Cailloux24, Glace_Cailloux25, Glace_Cailloux26, Glace_Cailloux27, Glace_Cailloux28, Glace_Cailloux29, Glace_Cailloux30, Glace_Cailloux31, Glace_Cailloux32, Glace_Cailloux33, Glace_Cailloux34, Glace_Cailloux35, Glace_Cailloux36, Glace_Cailloux37, Glace_Cailloux38, Glace_Cailloux39, Glace_Cailloux40]

J_x_decor_Glace = 0
J_y_decor_Glace = 0

Sortie_Liste_Glace = []

Marchand_Liste_Glace = []

Map_Glace = Salle(Pnj_List_Glace, Mob_List_Glace, Item_List_Glace, Map_Glace_Image, J_x_decor_Glace, J_y_decor_Glace, Hitbox_Glace, Sortie_Liste_Glace, Marchand_Liste_Glace)


# Déclaration des sorties
Sortie_Glace_Base = ChangeSalle(150, 350, "paillasson.png", Map_Base, 500, 500, 0, 0)
Sortie_Base_Glace = ChangeSalle(100, 100, "paillasson.png", Map_Glace, 0, 0, 500, 0)

# On met les sorties dans chaque Salle
Map_Base.a_Sortie_Liste.append(Sortie_Base_Glace)
Map_Glace.a_Sortie_Liste.append(Sortie_Glace_Base)


CurrentMap = Map_Base
Fond = CurrentMap.a_Image
screenWidth = 600
screenHeight = 600

Dialogue_x = 200
Dialogue_Y = 200

Perso_Hero = Hero(250, 250)   # Hero(screenWidth / 2 - 50, screenHeight / 2 - 50)

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

# Fonction pour verifier la hitbox


def inRects(perso):
    directionblock = [False, False, False, False]
    x = perso.aX
    y = perso.aY
    height, width = perso.aImage.get_height(), perso.aImage.get_width()
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
    height, width = perso.aImage.get_height(), perso.aImage.get_width()
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


###################################################################################
# Initialize pygame
pygame.init()

# set police for text
text_font = pygame.font.SysFont("arial", 50)
Gold_font = pygame.font.SysFont("arial", 20)

# Set the width and height of the screen [width,height]
screen = pygame.display.set_mode((screenWidth, screenHeight))

# Set title of screen
pygame.display.set_caption("Oui")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

pygame.mouse.set_visible(1)

# Programme principal
while not done:
    event = pygame.event.Event(pygame.USEREVENT)

    for event in pygame.event.get():  # User did something

        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    KeysPressed = pygame.key.get_pressed()

    # Déplacement du Hero si il n'est pas entrain de faire une autre action
    if Perso_Hero.a_Duree == 0:
        collision = inRects(Perso_Hero)
        collision_vitesse = inRectsVitesse(Perso_Hero)
        if KeysPressed[pygame.K_UP] and collision[3] is False:
            Perso_Hero.changei("HeroH")
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
            Perso_Hero.changei("Hero")
            if collision_vitesse[1] is not False:
                Perso_Hero.aY = collision_vitesse[1] - Perso_Hero.aImage.get_height() - CurrentMap.a_YDecor - 1
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
            Perso_Hero.changei("HeroG")
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
            Perso_Hero.changei("HeroD")
            if collision_vitesse[0] is not False:
                Perso_Hero.aX = collision_vitesse[0] - Perso_Hero.aImage.get_width() - CurrentMap.a_XDecor - 1
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
        Perso_Hero.a_Duree -= 1

# Pour éviter que le Perso sorte de l'écran
    if Perso_Hero.aX < 0:
        Perso_Hero.aX = 0
    if Perso_Hero.aY < 0:
        Perso_Hero.aY = 0
    if Perso_Hero.aX + Perso_Hero.aImage.get_width() > screenWidth:
        Perso_Hero.aX = screenWidth - Perso_Hero.aImage.get_width()
    if Perso_Hero.aY + Perso_Hero.aImage.get_height() > screenHeight:
        Perso_Hero.aY = screenHeight - Perso_Hero.aImage.get_height()
    hero_hitbox = (Perso_Hero.aX, Perso_Hero.aY, Perso_Hero.aImage.get_height(), Perso_Hero.aImage.get_width())

    for onecailloux in CurrentMap.a_Tab_Hitbox:
        onecailloux.affiche_aX = onecailloux.aX - CurrentMap.a_XDecor
        onecailloux.affiche_aY = onecailloux.aY - CurrentMap.a_YDecor
        pygame.draw.rect(screen, (255, 0, 0), (onecailloux.affiche_aX, onecailloux.affiche_aY, 50, 60), 2)

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
            print("Achat arme")
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
            print("Achat magie")
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
            for one_Mob in CurrentMap.a_Mob_List:
                one_Mob.getattack(Perso_Hero, CurrentMap.a_XDecor, CurrentMap.a_YDecor)

# Test si le perso est proche de la sortie, si oui le change de salle
    for one_Sortie in CurrentMap.a_Sortie_Liste:
        if Perso_Hero.aX + Perso_Hero.aImage.get_width() > one_Sortie.aX - CurrentMap.a_XDecor and Perso_Hero.aX < one_Sortie.aX + one_Sortie.a_Image.get_width() - CurrentMap.a_XDecor and Perso_Hero.aY + Perso_Hero.aImage.get_height() > one_Sortie.aY - CurrentMap.a_YDecor and Perso_Hero.aY < one_Sortie.aY + one_Sortie.a_Image.get_height() - CurrentMap.a_YDecor:
            CurrentMap = one_Sortie.a_Salle
            Fond = CurrentMap.a_Image
            CurrentMap.a_XDecor = one_Sortie.aX_Decor
            CurrentMap.a_YDecor = one_Sortie.aY_Decor
            Perso_Hero.aX = one_Sortie.aX_Perso
            Perso_Hero.aY = one_Sortie.aY_Perso

# Fond + caméra
    ZoneCam = pygame.Rect(CurrentMap.a_XDecor, CurrentMap.a_YDecor, screenWidth, screenHeight)
    screen.blit(Fond, (0, 0), area=ZoneCam)

# Affiche le perso
    screen.blit(Perso_Hero.aImage, (Perso_Hero.aX, Perso_Hero.aY))
    pygame.draw.rect(screen, (255, 0, 0), hero_hitbox, 2)
    pygame.draw.rect(screen, (255, 0, 255), (Perso_Hero.aX - Perso_Hero.vitesse, Perso_Hero.aY - Perso_Hero.vitesse, Perso_Hero.aImage.get_height() + 2*Perso_Hero.vitesse, Perso_Hero.aImage.get_width() + 2*Perso_Hero.vitesse), 2)

# Affichage de chaque pnj / Mob et Sortie de la pièce courante
    for one_Pnj in CurrentMap.a_Pnj_List:
        screen.blit(one_Pnj.aImage, (one_Pnj.aX - CurrentMap.a_XDecor, one_Pnj.aY - CurrentMap.a_YDecor))

    for one_Mob in CurrentMap.a_Mob_List:
        if one_Mob.a_health > 0:
            one_Mob.move(Perso_Hero.aX + CurrentMap.a_XDecor, Perso_Hero.aY + CurrentMap.a_YDecor)
            one_Mob.attaque(Perso_Hero, CurrentMap.a_XDecor, CurrentMap.a_YDecor)
            screen.blit(one_Mob.aImage, (one_Mob.aX - CurrentMap.a_XDecor, one_Mob.aY - CurrentMap.a_YDecor))
        else:
            Perso_Hero.a_exp += one_Mob.xp
            CurrentMap.a_Mob_List.remove(one_Mob)
    for one_Sortie in CurrentMap.a_Sortie_Liste:
        screen.blit(one_Sortie.a_Image, (one_Sortie.aX - CurrentMap.a_XDecor, one_Sortie.aY - CurrentMap.a_YDecor))
    for one_marchant in CurrentMap.a_Marchand_Liste:
        screen.blit(one_marchant.aImage, (one_marchant.aX - CurrentMap.a_XDecor, one_marchant.aY - CurrentMap.a_YDecor))
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

    for onecailloux in CurrentMap.a_Tab_Hitbox:
        pygame.draw.rect(screen, (255, 0, 0), (onecailloux.affiche_aX, onecailloux.affiche_aY, 50, 60), 2)

    if Perso_Hero.actulvl():
        done_lvl = False
        points_lvl = 10
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
            text = Gold_font.render(" Augmente ton mana max de 10", True, [255, 255, 255])
            screen.blit(text, (110, 130))
            text = Gold_font.render(" Augmente ta force de 5", True, [255, 255, 255])
            screen.blit(text, (110, 230))
            text = Gold_font.render("  Augmente ta defense de 5", True, [255, 255, 255])
            screen.blit(text, (110, 330))
            text = Gold_font.render(" Augmente ton intelligence de 5", True, [255, 255, 255])
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
    gold_text = Gold_font.render("Gold : " + str(Perso_Hero.a_gold), True, [255, 0, 255])
    screen.blit(gold_text, (0, 570))

    # test pour chaque pnj si le joueur est assez proche pour afficher le dialogue
    for one_Pnj in CurrentMap.a_Pnj_List:
        zone_text = text_font.render(Perso_Hero.dialogue(one_Pnj, CurrentMap.a_XDecor, CurrentMap.a_YDecor), True, [255, 255, 0])
        screen.blit(zone_text, (0, 500))

    if Perso_Hero.a_health <= 0:
        done = True
    # 60 fps
    clock.tick(30)
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

pygame.quit()
