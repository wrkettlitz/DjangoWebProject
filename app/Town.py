



class Town():


    def __init__(self, name, amount_of_buildings, amount_of_barracks, resources, money, level, ID,amount_of_soldiers):
        self.name = name
        self.amount_of_buildings = amount_of_buildings
        self.amount_of_barracks = amount_of_barracks
        self.resources = resources
        self.money = money
        self.level = level
        self.ID = ID
        self.amount_of_soldiers=amount_of_soldiers

    def addBarrack(self, amount):
        if self.money >= (200 * amount):
            self.money -= (200 * amount)
            self.amount_of_barracks += amount

            if self.amount_of_barracks == 1:
                self.level += 1

            return self.amount_of_barracks
        else:
            return False

    def addSoldier(self, amount):
        if self.money >= (100 * amount):
                self.money -= (100 * amount)
                self.amount_of_soldiers += amount
                return self.amount_of_soldiers

        else:
                return False


# Misschien in de database een uniek ID per persoon, en dit dan in de class instantie doen. Ofzo.
T = Town("TestTown", 10, 0, "No resources", 900, 0, 0,0)



