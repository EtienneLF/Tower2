import Class.Perso


class Mob(Class.Perso.Perso):
    def __init__(self, px, py, p_health, p_image):
        Class.Perso.Perso.__init__(self, px, py, p_image)
        self.a_health = p_health

    def getattack(self, p_hero):
        if self.aX - 10 < p_hero.aX < self.aX + self.aImage.get_width() + 10 and self.aY - 10 < p_hero.aY < self.aY + self.aImage.get_height() + 10:
            print("degats =" + str(p_hero.a_strength))
            self.a_health -= p_hero.a_strength
