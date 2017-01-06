#not used

class Player():

    def __init__(self, name, money):
        self.name = name
        self.money = money

    def GetName(self):
        return self.name

    def SetName(self, name):
        name = self.name


    def GetMoney(self):
        return self.money

    def SetMoney(self,money):
        money = self.money


    def buyBarrack(self, amount):
        self.money -= (200 * amount)
        return self.money

P = Player("TestPlayer", 1000)  