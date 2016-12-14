class Player:
    name = ""
    money = int

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
        