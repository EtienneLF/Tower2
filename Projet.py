import inspect
import os

import pygame

from Class.Hero import Hero
from Class.Mob import Mob
from Class.Perso import Pnj, MarchandArme, MarchandMagie
from Class.Salle import Salle, ChangeSalle
from Class.Shop import Shop
from Class.Item import Epee, Bottes, Armure
from Class.Cailloux import Cailloux

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
Sandales = Bottes("Sandales", 1, 5, "Au moins si vous marchez dans la boue tout ira bien")
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
Mob_1 = Mob(0, 0, 100, "Megumin.png")
Mob_1.aImage = pygame.transform.scale(Megumin.aImage, (100, 160))

# Création cailloux
Glace_Cailloux1 = Cailloux(300, 300)

# Position de la fenêtre
J_x_decor_Base = 0
J_y_decor_Base = 0

Pnj_List_Base = [Megumin]

Mob_List_Base = [Mob_1]

Item_List_Base = []

Hitbox_Base = []

Sortie_Liste_Base = []

Marchand_Liste_Base = [Marchand_Arme, Marchand_Magie]

Map_Base = Salle(Pnj_List_Base, Mob_List_Base, Item_List_Base, Map_Base_Image, J_x_decor_Base, J_y_decor_Base, Hitbox_Base, Sortie_Liste_Base, Marchand_Liste_Base)

# Création salle dde glace
Pnj_List_Glace = []

Mob_List_Glace = []

Item_List_Glace = []

Hitbox_Glace = [Glace_Cailloux1]

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

Perso_Hero = Hero(250, 250)   # Hero(screenWidth / 2 - 50, screenHeight / 2 - 53)

# Attribut pour savoir si on a ouvert un shop
AucunShop = 0
Shop_Arme = 1
Shop_Magie = 2
CurrentShop = 0

# Fonction pour équiper un item


def equipe(p_hero, p_item):
    if p_item.ckoi() == "Epee":
        p_hero.a_weapon = p_item
    elif p_item.ckoi() == "Bottes":
        p_hero.a_armor = p_item
    else:
        p_hero.a_boot = p_item
    Perso_Hero.actustat()


###################################################################################
# Initialize pygame
pygame.init()

# set police for text
text_font = pygame.font.SysFont("arial", 50)

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

    # Deplacement du Hero si il n'est pas entrain de faire une autre action
    if Perso_Hero.a_Duree == 0:

        if KeysPressed[pygame.K_UP]:
            Perso_Hero.changei("HeroH")
            if Perso_Hero.aY > screenHeight / 2 - 53:
                Perso_Hero.aY -= Perso_Hero.vitesse
                if Perso_Hero.aY < screenHeight / 2 - 53:
                    Perso_Hero.aY = screenHeight / 2 - 53
            else:
                CurrentMap.a_YDecor -= Perso_Hero.vitesse
                if CurrentMap.a_YDecor < 0:
                    CurrentMap.a_YDecor = 0
                    Perso_Hero.aY -= Perso_Hero.vitesse

        if KeysPressed[pygame.K_DOWN]:
            Perso_Hero.changei("Hero")
            if Perso_Hero.aY < screenHeight / 2 - 53:
                Perso_Hero.aY += Perso_Hero.vitesse
                if Perso_Hero.aY > screenHeight / 2 - 53:
                    Perso_Hero.aY = screenHeight / 2 - 53
            else:
                CurrentMap.a_YDecor += Perso_Hero.vitesse
                if CurrentMap.a_YDecor + screenHeight > Fond.get_height():
                    CurrentMap.a_YDecor = Fond.get_height() - screenHeight
                    Perso_Hero.aY += Perso_Hero.vitesse

        if KeysPressed[pygame.K_LEFT]:
            Perso_Hero.changei("HeroG")
            if Perso_Hero.aX > screenWidth / 2 - 50:
                Perso_Hero.aX -= Perso_Hero.vitesse
                if Perso_Hero.aX < screenWidth / 2 - 50:
                    Perso_Hero.aX = screenWidth / 2 - 50
            else:
                CurrentMap.a_XDecor -= Perso_Hero.vitesse
                if CurrentMap.a_XDecor < 0:
                    CurrentMap.a_XDecor = 0
                    Perso_Hero.aX -= Perso_Hero.vitesse

        if KeysPressed[pygame.K_RIGHT]:
            Perso_Hero.changei("HeroD")
            if Perso_Hero.aX < screenWidth / 2 - 50:
                Perso_Hero.aX += Perso_Hero.vitesse
                if Perso_Hero.aX > screenWidth / 2 - 50:
                    Perso_Hero.aX = screenWidth / 2 - 50
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
    herohitbox = (Perso_Hero.aX + 5, Perso_Hero.aY, 50, 60)

    for onecailloux in CurrentMap.a_Tab_Hitbox :
        onecailloux.affiche_aX = onecailloux.aX - CurrentMap.a_XDecor
        onecailloux.affiche_aY = onecailloux.aY - CurrentMap.a_YDecor
        pygame.draw.rect(screen, (255, 0, 0), (Glace_Cailloux1.affiche_aX, Glace_Cailloux1.affiche_aY, 50, 60), 2)

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
            if 10 <= y <= 193 and Perso_Hero.a_gold:
                if Shop_Arme_Base.a_Item1 is not None:
                    equipe(Perso_Hero, Shop_Arme_Base.a_Item1)
                    Shop_Arme_Base.a_Item1 = None
            elif 193 <= y <= 193*2:
                if Shop_Arme_Base.a_Item2 is not None:
                    equipe(Perso_Hero, Shop_Arme_Base.a_Item2)
                    Shop_Arme_Base.a_Item2 = None
            elif 193*2 <= y <= 193*3:
                if Shop_Arme_Base.a_Item3 is not None:
                    equipe(Perso_Hero, Shop_Arme_Base.a_Item3)
                    Shop_Arme_Base.a_Item3 = None

    elif CurrentShop == Shop_Magie:
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Achat magie")
            pos = pygame.mouse.get_pos()
            y = pos[1]
            if 10 <= y <= 193:
                Shop_Magie_Base.a_Item1 = None
            elif 193 <= y <= 193*2:
                Shop_Magie_Base.a_Item2 = None
            elif 193*2 <= y <= 193*3:
                Shop_Magie_Base.a_Item3 = None
    else:
        # Test si clic gauche, si oui met le sprite attaque et test si un mob est proche
        if event.type == pygame.MOUSEBUTTONDOWN and Perso_Hero.a_Duree == 0:
            Perso_Hero.attaque()
            for one_Mob in CurrentMap.a_Mob_List:
                one_Mob.getattack(Perso_Hero)

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
    pygame.draw.rect(screen, (255, 0, 0), herohitbox, 2)
# Affichage de chaque pnj / Mob et Sortie de la pièce courante
    for one_Pnj in CurrentMap.a_Pnj_List:
        screen.blit(one_Pnj.aImage, (one_Pnj.aX - CurrentMap.a_XDecor, one_Pnj.aY - CurrentMap.a_YDecor))

    for one_Mob in CurrentMap.a_Mob_List:
        if one_Mob.a_health > 0:
            screen.blit(one_Mob.aImage, (one_Mob.aX - CurrentMap.a_XDecor, one_Mob.aY - CurrentMap.a_YDecor))
        else:
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

    # test pour chaque pnj si le joueur est assez proche pour afficher le dialogue
    for one_Pnj in CurrentMap.a_Pnj_List:
        zone_text = text_font.render(Perso_Hero.dialogue(one_Pnj, CurrentMap.a_XDecor, CurrentMap.a_YDecor), True, [255, 255, 0])
        screen.blit(zone_text, (0, 500))

    # 60 fps
    clock.tick(30)
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

pygame.quit()
