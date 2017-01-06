class Soldier:
    name = ""
    health_bar = int
    damage = int
    price = int

    def __init__(self, name, health_bar, damage, price):
        self.name = name
        self.health_bar = health_bar
        self.damage = damage
        self.price = price


    def GetName(self):
        return self.name

    def SetName(self, name):
        name = self.name
    def GetHealthBar(self):
        return self.health_bar

    def SetHealthBar(self, health_bar):
        health_bar = self.health_bar

    def GetDamage(self):
        return self.damage

    def SetDamage(self, damage):
        damage = self.damage

    def GetPrice(self):
            return self.price

    def SetPrice(self, price):
            price = self.price



