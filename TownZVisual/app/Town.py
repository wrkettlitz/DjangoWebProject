
class Town():


    def __init__(self, name, amount_of_buildings, amount_of_barracks, resources, money, level, ID):
        self.name = name
        self.amount_of_buildings = amount_of_buildings
        self.amount_of_barracks = amount_of_barracks
        self.resources = resources
        self.money = money
        self.level = level
        self.ID = ID

    def addBarrack(self, amount):
        if self.money >= (200 * amount):
            self.money -= (200 * amount)
            self.amount_of_barracks += amount

            if self.amount_of_barracks == 1:
                self.level += 1

            return self.amount_of_barracks
        else:
            return False


    def GetName(self):
        return self.name

    def SetName(self,name):
        name = self.name

    def GetAmount_of_Buildings(self):
        return self.amount_of_buildings

    def SetAmount_of_buildings(self,amount_of_buildings):
        amount_of_buildings = self.amount_of_buildings

    def GetAmount_of_Barracks(self):
        return self.amount_of_barracks

    def SetAmount_of_Barracks(self,amount_of_barracks):
        amount_of_barracks = self.amount_of_barracks

    def GetResources(self):
        return self.resources

    def SetResources(self,resources):
        resources = self.resources

    def GetMoney(self):
        return self.money

    def SetMoney(self,money):
        money = self.money


# Misschien in de database een uniek ID per persoon, en dit dan in de class instantie doen. Ofzo.
T = Town("TestTown", 10, 0, "No resources", 900, 0, 0)



