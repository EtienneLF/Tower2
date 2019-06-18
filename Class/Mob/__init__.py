import Class.Perso
import random


class Mob(Class.Perso.Perso):
    def __init__(self, px, py, p_health, p_image, p_vitesse, p_distance, p_xp, p_attaque):
        Class.Perso.Perso.__init__(self, px, py, p_image)
        self.a_health = p_health
        self.a_vitesse = p_vitesse
        self.d_X = 0
        self.d_Y = 0
        self.temps = 0
        self.tempsAttaque = 1
        self.distance = p_distance
        self.xp = p_xp
        self.attack = p_attaque
        self.mode_a = False

    def getattack(self, p_hero, p_x, p_y):
        if self.aX - 10 < p_hero.aX + p_x < self.aX + self.aImage.get_width() + 10 and self.aY - 10 < p_hero.aY + p_y < self.aY + self.aImage.get_height() + 10:
            print("degats =" + str(p_hero.a_strength))
            self.a_health -= p_hero.a_strength

    def attaque(self, p_hero, p_x, p_y):
        if self.tempsAttaque <= 0:
            if p_hero.aX + p_x == self.aX and p_hero.aY + p_y == self.aY:
                p_hero.a_health -= self.attack
                self.tempsAttaque = 60
            else:
                self.tempsAttaque = 0
        else:
            self.tempsAttaque -= 1

    def random_move(self):
        move_x = random.randint(0, 2)
        move_y = random.randint(0, 2)
        if move_x == 1:
            self.d_X = self.a_vitesse
        elif move_x == 2:
            self.d_X = -self.a_vitesse
        else:
            self.d_X = 0
        if move_y == 1:
            self.d_Y = self.a_vitesse
        elif move_y == 2:
            self.d_Y = -self.a_vitesse
        else:
            self.d_Y = 0

    def move(self, p_x, p_y):
        if self.aX - self.distance < p_x < self.aX + self.aImage.get_width() + self.distance and self.aY - self.distance < p_y < self.aY + self.aImage.get_height() + self.distance:
            self.mode_a = True
        if self.mode_a:
            if self.aX < p_x:
                self.d_X = self.a_vitesse
                if self.aX > p_x:
                    self.d_X = 0
                    self.aX = p_x
            elif self.aX > p_x:
                self.d_X = -self.a_vitesse
                if self.aX < p_x:
                    self.d_X = 0
                    self.aX = p_x
            else:
                self.d_X = 0

            if self.aY < p_y:
                self.d_Y = self.a_vitesse
                if self.aY > p_y:
                    self.d_Y = 0
                    self.aY = p_y
            elif self.aY > p_y:
                self.d_Y = -self.a_vitesse
                if self.aY < p_y:
                    self.d_Y = 0
                    self.aY = p_y
            else:
                self.d_Y = 0

            self.aX += self.d_X
            self.aY += self.d_Y
        else:
            if self.temps > 0:
                self.aX += self.d_X
                self.aY += self.d_Y
                self.temps -= 1
            else:
                self.random_move()
                self.temps = 30
