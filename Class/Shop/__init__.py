import pygame

pygame.init()
text_font = pygame.font.SysFont("arial", 20)


class Shop:
    def __init__(self, p_item1, p_item2, p_item3):
        self.a_Item1 = p_item1
        self.a_Item2 = p_item2
        self.a_Item3 = p_item3

    def dessine(self, p_screen):
        if self.a_Item1 is not None:
            p_screen.blit(self.a_Item1.a_Image, (self.a_Item1.a_Image.get_width() - 80, self.a_Item1.a_Image.get_height() - 50))
            zone_text = text_font.render(self.a_Item1.a_Name + " :", True, [255, 255, 255])
            p_screen.blit(zone_text, (250, 20))
            zone_text = text_font.render(self.a_Item1.a_Description, True, [255, 255, 255])
            p_screen.blit(zone_text, (200, 60))
            zone_text = text_font.render("Prix : " + str(self.a_Item1.a_Prix) + " Or", True, [255, 255, 255])
            p_screen.blit(zone_text, (200, 100))
        else:
            zone_text = text_font.render(" VIDE ", True, [255, 255, 255])
            p_screen.blit(zone_text, (290, 100))

        if self.a_Item2 is not None:
            p_screen.blit(self.a_Item2.a_Image, (self.a_Item2.a_Image.get_width() - 80, self.a_Item2.a_Image.get_height() + 143))
            zone_text = text_font.render(self.a_Item2.a_Name + " :", True, [255, 255, 255])
            p_screen.blit(zone_text, (250, 193))
            zone_text = text_font.render(self.a_Item2.a_Description, True, [255, 255, 255])
            p_screen.blit(zone_text, (200, 233))
            zone_text = text_font.render("Prix : " + str(self.a_Item2.a_Prix) + " Or", True, [255, 255, 255])
            p_screen.blit(zone_text, (200, 273))
        else:
            zone_text = text_font.render(" VIDE ", True, [255, 255, 255])
            p_screen.blit(zone_text, (290, 273))

        if self.a_Item3 is not None:
            p_screen.blit(self.a_Item3.a_Image, (self.a_Item3.a_Image.get_width() - 80, self.a_Item3.a_Image.get_height() + 340))
            zone_text = text_font.render(self.a_Item3.a_Name + " :", True, [255, 255, 255])
            p_screen.blit(zone_text, (250, 390))
            zone_text = text_font.render(self.a_Item3.a_Description, True, [255, 255, 255])
            p_screen.blit(zone_text, (200, 430))
            zone_text = text_font.render("Prix : " + str(self.a_Item3.a_Prix) + " Or", True, [255, 255, 255])
            p_screen.blit(zone_text, (200, 470))
        else:
            zone_text = text_font.render(" VIDE ", True, [255, 255, 255])
            p_screen.blit(zone_text, (290, 470))
