class Cailloux:
    def __init__(self, px, py):
        self.aX = px
        self.aY = py
        self.affiche_aX = px
        self.affiche_aY = py
        self.Hitbox = (self.aX, self.aY, 50, 60)

    def inRect(self, pixel):
        x, y = pixel
        if self.affiche_aX <= x <= self.affiche_aX + 50 and self.affiche_aY <= y <= self.affiche_aY + 60:
            return True
        else:
            return False
