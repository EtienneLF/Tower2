class Item:
    def __init__(self, p_name, p_prix, p_stat, p_description):
        self.a_Name = p_name
        self.a_Prix = p_prix
        self.a_Stat = p_stat
        self.a_Description = p_description
        self.a_Image = None


class Epee(Item):
    def __init__(self, p_name, p_prix, p_stat, p_description):
        Item.__init__(self, p_name, p_prix, p_stat, p_description)

    @staticmethod
    def ckoi():
        return "Epee"


class Bottes(Item):
    def __init__(self, p_name, p_prix, p_stat, p_description):
        Item.__init__(self, p_name, p_prix, p_stat, p_description)

    @staticmethod
    def ckoi():
        return "Bottes"


class Armure(Item):
    def __init__(self, p_name, p_prix, p_stat, p_description):
        Item.__init__(self, p_name, p_prix, p_stat, p_description)

    @staticmethod
    def ckoi():
        return "Armure"
