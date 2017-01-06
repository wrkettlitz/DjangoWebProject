class Barrack:
    amountofsoldiers = int
    name = ""

    def __init__(self,amountofsoldiers, name):
        self.amountofsoldiers = amountofsoldiers
        self.name = name

    def GetAmountofSoldiers(self):
       return self.amountofsoldiers

    def SetAmountofSoldiers(self,amountofsoldiers):
         amountofsoldiers = self.amountofsoldiers

    def GetName(self):
        return self.name

    def SetName(self, name):
        name = self.name


