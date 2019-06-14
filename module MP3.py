#module utilisant Empire comme base, pas d'overlapping des musiques
# press num0 ou space pour differentes musique (si path correspondant)

import pygame
from pygame import mixer
import os, inspect
from pygame.transform import scale
from random import *
import math

#recherche du répertoire de travail
scriptPATH = os.path.abspath(inspect.getsourcefile(lambda:0)) # compatible interactive Python Shell
scriptDIR  = os.path.dirname(scriptPATH)
assets = os.path.join(scriptDIR,"data")


# Setup
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

police = pygame.font.SysFont("arial", 15)
 
 
print(scriptDIR)
 
 
# Set the width and height of the screen [width,height]
screeenWidth = 400
screenHeight = 300
screen = pygame.display.set_mode((screeenWidth,screenHeight))
pygame.display.set_caption("Empire City")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# timer t0 en secondes
t0 = int(pygame.time.get_ticks()/1000)
 
# Hide the mouse cursor
pygame.mouse.set_visible(True) 
 
fond = pygame.image.load(os.path.join(assets, "map.png"))
viseur = pygame.image.load(os.path.join(assets, "viseur.png"))

b_rue1 = pygame.image.load(os.path.join(assets, "bandit_rue2.png"))
b_fen1 = pygame.image.load(os.path.join(assets, "bandit_window4.png"))

bang = pygame.image.load(os.path.join(assets, "bang.png"))
fleched = pygame.image.load(os.path.join(assets, "fleche_droite.png"))
flecheg = pygame.image.load(os.path.join(assets, "fleche_gauche.png"))

J_xdecor = 350 # coord verticale zone jaune
J_ydecor = 170 # coord horizontale zone jaune

V_xecran =  (screeenWidth/2) - (viseur.get_width()/2) #coord viseur
V_yecran =  (screenHeight/2) - (viseur.get_height()/2) #coord viseur


V_xdecor = J_xdecor + V_xecran
V_ydecor = J_ydecor + V_yecran
 
t0 =  int(pygame.time.get_ticks()/1000)
reset = 0 
bandit_vivant1=0 # mort = 0 vivant = 1
bandit_vivant2=0 # mort = 0 vivant = 1

tirage1 = 0 # pos aléatoire, 0 si pas tiré et 1 si oui
stillalive1 = 0 #ennemi 1 tjrs vivant si 1, 0 si non
stillalive2 = 0 #ennemi 1 tjrs vivant si 1, 0 si non
choix = 2

posx2 = 0
posy2 = 0
random = randint(1,4)
hasard2 = randint(1,2)
# -------- Main Program Loop -----------
while not done:
   event = pygame.event.Event(pygame.USEREVENT)    # Remise à zero de la variable event
   
    # DESSIN 
    
   # affiche la zone de rendu au dessus de fenetre de jeu
   zonejaune = pygame.Rect( J_xdecor, J_ydecor, screeenWidth, screenHeight )
   screen.blit(fond,(0,0),area = zonejaune)
   
   
   # bandit rue
    
   timebr1 = int(pygame.time.get_ticks()/1000)
   timebr2 = int(pygame.time.get_ticks()/1000)
   if(hasard2==1):
      choix = 0
      if((timebr1 % 3) == 0 and tirage1 == 0):
         posx = randint(10,1700) 
         tirage1 = 1
      
      if ((timebr1 % 6) == 0  or stillalive1 == 1):
         screen.blit(b_rue1,(posx-J_xdecor,500-J_ydecor))
         stillalive1 = 1
         
   elif(hasard2==2):
      choix = 1
      if((timebr2 % 3) == 0 and tirage1 == 0):
         
         print(random)
         if(random==1):
            posx2 = 800
            posy2 = 300
            print(posx2)
            print(posy2)
         if(random==2): 
            posx2 = 980
            posy2 = 300
            print(posx2)
            print(posy2)
         if(random==3 ): 
            posx2 = 1200
            posy2 = 450
            print(posx2)
            print(posy2)
         if(random==4 ): 
            posx2 = 1360
            posy2 = 260
            print(posx2)
            print(posy2)
         tirage1 = 1
      
      
      
      if(tirage1 == 1):
         if ((timebr2 % 6) == 0  or stillalive2 == 1):
            screen.blit(b_fen1,(posx2-J_xdecor,posy2-J_ydecor))
            stillalive2 = 1
   

   # flèches
   if(choix == 0):
      if(stillalive1 == 1 and (((posx-J_xdecor)-(V_xecran +10)) + ((500-J_ydecor)-(V_yecran+ 10)))>= 200):
         screen.blit(fleched,(350,150))
   
      if(stillalive1 == 1 and (((posx-J_xdecor)-(V_xecran +10)) + ((500-J_ydecor)-(V_yecran+ 10)))<= -200):
         screen.blit(flecheg,(0,150))
      
   if(choix == 1):
      if(stillalive2 == 1 and (((posx2-J_xdecor)-(V_xecran +10)) + ((posy2-J_ydecor)-(V_yecran+ 10)))>= 200):
         screen.blit(fleched,(350,150))
   
      if(stillalive2 == 1 and (((posx2-J_xdecor)-(V_xecran +10)) + ((posy2-J_ydecor)-(V_yecran+ 10)))<= -200):
         screen.blit(flecheg,(0,150))
   # dessin avant plan
   
   
   screen.blit(viseur,(V_xecran,V_yecran))
  


   # récupère la liste des touches claviers appuyeées sous la forme liste bool
   pygame.event.pump()
   
   KeysPressed = pygame.key.get_pressed()
   
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         done = True
      
   if KeysPressed[pygame.K_UP]:
      if(V_yecran >= 4):
         V_yecran -= 4
         if (J_ydecor > 0):
            if(V_yecran  <= 50):
               J_ydecor -= 10
               V_yecran += 4
         
   if KeysPressed[pygame.K_DOWN]:
      if(V_yecran <= 240):
         V_yecran += 4
         if (J_ydecor < 380 ):
            if(V_yecran  >= 200):
               J_ydecor += 10
               V_yecran -= 4
      
   if KeysPressed[pygame.K_LEFT]:
      if(V_xecran >= 4):
         V_xecran -= 4
         if (J_xdecor > 0):
            if(V_xecran  <= 50):
               J_xdecor -= 10
               V_xecran += 4
      
   if KeysPressed[pygame.K_RIGHT]:
      if(V_xecran <= 350):
         V_xecran += 4
         if (J_xdecor < 1600 ):
            if(V_xecran  >= 300):
               J_xdecor += 10
               V_xecran -= 4
      
   if KeysPressed[pygame.K_SPACE]:
      mixer.init()
      mixer.music.load('C:/Users/ivanoffj/Music/BattleMusic1 (DGRP2).mp3')
      mixer.music.play() 
      screen.blit(bang,(V_xecran +10,V_yecran+ 10))
      if(choix == 0):
            dist = math.sqrt(((posx-J_xdecor)-(V_xecran +10))*((posx-J_xdecor)-(V_xecran +10)) + ((500-J_ydecor)-(V_yecran+ 10))*((500-J_ydecor)-(V_yecran+ 10)))
      recul = randint(1,2)
      if(choix == 1):
            dist = math.sqrt(((posx2-J_xdecor)-(V_xecran +10))*((posx2-J_xdecor)-(V_xecran +10)) + ((posy2-J_ydecor)-(V_yecran+ 10))*((posy2-J_ydecor)-(V_yecran+ 10)))
      if(recul ==1):
         V_yecran = V_yecran - 10
      if((dist<=50)):
          bandit_vivant1 = 0 
          tirage1 = 0
          stillalive1= 0
          hasard2 = randint(1,2)
          random = randint(1,4)
          


    # LOGIQUE  
   
   
   
 

 
   
   

    # Go ahead and update the screen with what we've drawn.
   pygame.display.flip()
 
    # Limit frames per second
   clock.tick(60)
 
# Close the window and quit.
pygame.quit()
