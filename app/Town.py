class Town:
    name = ""
    amount_of_buildings = int
    amount_of_barracks = int
    resources = ""


    def __init__(self,name,amount_of_buildings,amount_of_barracks,resources):
        self.name = name
        self.amount_of_buildings = amount_of_buildings
        self.amount_of_barracks = amount_of_barracks
        self.resources = resources

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

