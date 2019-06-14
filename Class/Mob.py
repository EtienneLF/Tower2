import Class.Perso


class Mob(Class.Perso.Perso):
    def __init__(self, px, py, p_health, p_image):
        Class.Perso.Perso.__init__(self, px, py, p_image)
        self.a_health = p_health

    def getattack(self, phero):
        if self.aX - 10 < phero.aX < self.aX + self.aImage.get_width() + 10 and self.aY - 10 < phero.aY < self.aY + self.aImage.get_height() + 10:
            print("degats =" + str(phero.a_strength * phero.a_Puissance_stuff))
            self.a_health -= phero.a_strength * phero.a_Puissance_stuff
