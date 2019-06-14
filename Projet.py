from Class.Perso import Pnj
from Class.Hero import Hero
from Class.Mob import Mob
from Class.Salle import Salle
import os
import inspect
import pygame

# recherche du repertoire de travail bonjour

scriptPATH = os.path.abspath(inspect.getsourcefile(lambda: 0))  # compatible interactive Python Shell
scriptDIR = os.path.dirname(scriptPATH)
assets = os.path.join(scriptDIR, "data")

Map_Base = pygame.image.load(os.path.join(assets, "Carte.jpg"))
Map_Neige = pygame.image.load(os.path.join(assets, "Glace.PNG"))
Map_Lave = pygame.image.load(os.path.join(assets, "Lave.PNG"))

Fond = Map_Base


screenWidth = 1000
screenHeight = 800

Perso_Hero = Hero(screenWidth / 2 - 50, screenHeight / 2 - 53)

Megumin = Pnj(1125, 450, "Megumin.png", "Bonjour EXPLOSION")
Megumin.aImage = pygame.transform.scale(Megumin.aImage, (100, 160))

Mob_1 = Mob(0, 0, 100, "Megumin.png")
Mob_1.aImage = pygame.transform.scale(Megumin.aImage, (100, 160))

J_x_decor = 500
J_y_decor = 500  # Fond.get_height()- screenHeight&

# Les différentes listes

Pnj_List = [Megumin]

Mob_List = [Mob_1]

Item_List =[]


###################################################################################
# Initialize pygame
pygame.init()

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

    # Deplacement du Hero
    if Perso_Hero.aDuree == 0:

        if KeysPressed[pygame.K_UP]:
            Perso_Hero.changei("HeroH")
            if Perso_Hero.aY > screenHeight / 2 - 53:
                Perso_Hero.aY -= Perso_Hero.vitesse
                if Perso_Hero.aY < screenHeight / 2 - 53:
                    Perso_Hero.aY = screenHeight / 2 - 53
            else:
                J_y_decor -= Perso_Hero.vitesse
                if J_y_decor < 0:
                    J_y_decor = 0
                    Perso_Hero.aY -= Perso_Hero.vitesse

        if KeysPressed[pygame.K_DOWN]:
            Perso_Hero.changei("Hero")
            if Perso_Hero.aY < screenHeight / 2 - 53:
                Perso_Hero.aY += Perso_Hero.vitesse
                if Perso_Hero.aY > screenHeight / 2 - 53:
                    Perso_Hero.aY = screenHeight / 2 - 53
            else:
                J_y_decor += Perso_Hero.vitesse
                if J_y_decor + screenHeight > Fond.get_height():
                    J_y_decor = Fond.get_height() - screenHeight
                    Perso_Hero.aY += Perso_Hero.vitesse

        if KeysPressed[pygame.K_LEFT]:
            Perso_Hero.changei("HeroG")
            if Perso_Hero.aX > screenWidth / 2 - 50:
                Perso_Hero.aX -= Perso_Hero.vitesse
                if Perso_Hero.aX < screenWidth / 2 - 50:
                    Perso_Hero.aX = screenWidth / 2 - 50
            else:
                J_x_decor -= Perso_Hero.vitesse
                if J_x_decor < 0:
                    J_x_decor = 0
                    Perso_Hero.aX -= Perso_Hero.vitesse

        if KeysPressed[pygame.K_RIGHT]:
            Perso_Hero.changei("HeroD")
            if Perso_Hero.aX < screenWidth / 2 - 50:
                Perso_Hero.aX += Perso_Hero.vitesse
            if Perso_Hero.aX > screenWidth / 2 - 50:
                Perso_Hero.aX = screenWidth / 2 - 50
            else:
                J_x_decor += Perso_Hero.vitesse
                if J_x_decor + screenWidth > Fond.get_width():
                    J_x_decor = Fond.get_width() - screenWidth
                    Perso_Hero.aX += Perso_Hero.vitesse
    else:
        Perso_Hero.aDuree -= 1

    if Perso_Hero.aX < 0:
        Perso_Hero.aX = 0
    if Perso_Hero.aY < 0:
        Perso_Hero.aY = 0
    if Perso_Hero.aX + 100 > screenWidth:
        Perso_Hero.aX = screenWidth - 100
    if Perso_Hero.aY + 107 > screenHeight:
        Perso_Hero.aY = screenHeight - 107

    if event.type == pygame.MOUSEBUTTONDOWN:
        Perso_Hero.attaque()
        for one_Mob in Mob_List:
            one_Mob.getattack(Perso_Hero)

    for one_Pnj in Pnj_List:
        Perso_Hero.dialogue(one_Pnj, J_x_decor)
    # Creation d'une zone
    ZoneCam = pygame.Rect(J_x_decor, J_y_decor, screenWidth, screenHeight)
    screen.blit(Fond, (0, 0), area=ZoneCam)

    for one_Pnj in Pnj_List:
        screen.blit(one_Pnj.aImage, (one_Pnj.aX - J_x_decor, one_Pnj.aY - J_y_decor))
    for one_Mob in Mob_List:
        if one_Mob.a_health > 0:
            screen.blit(one_Mob.aImage, (one_Mob.aX - J_x_decor, one_Mob.aY - J_y_decor))
    # Affiche le perso
    screen.blit(Perso_Hero.aImage, (Perso_Hero.aX, Perso_Hero.aY))

    # 60 fps
    clock.tick(30)
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

pygame.quit()
