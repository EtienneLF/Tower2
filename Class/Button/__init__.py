class Button:
    def __init__(self, p_image, px, py):
        self.a_image = p_image
        self.a_x = px
        self.a_y = py

    def appuie(self, px, py):
        if self.a_x < px < self.a_x + self.a_image.get_width() and self.a_y < py < self.a_y + self.a_image.get_height():
            return self.activer()

    def activer(self):
        return


class Button_lvl(Button):
    def __init__(self, p_image, px, py):
        Button.__init__(self, p_image, px, py)

    def activer(self):
        return True
