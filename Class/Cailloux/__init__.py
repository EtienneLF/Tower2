class Cailloux:
    def __init__(self, px, py):
        self.aX = px
        self.aY = py
        self.affiche_aX = px
        self.affiche_aY = py
        self.Hitbox = (self.aX + 5, self.aY, 50, 60)



