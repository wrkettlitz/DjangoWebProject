class Town:
    name = ""
    health_bar = int
    amount_of_barracks = int
    resources = ""

    def __init__(self,name,health_bar,amount_of_barracks,resources):
        self.name = name
        self.health_bar = health_bar
        self.amount_of_barracks = amount_of_barracks
        self.resources = resources

    def GetName(self):
        return self.name

    def SetName(self,name):
        name = self.name

    def GetHealth_Bar(self):
        return self.health_bar

    def SetHealth_Bar(self,heath_bar):
        heath_bar = self.health_bar

    def GetAmount_of_Barracks(self):
        return self.amount_of_barracks

    def SetAmount_of_Barracks(self,amount_of_barracks):
        amount_of_barracks = self.amount_of_barracks

    def GetResources(self):
        return self.resources

    def SetResources(self,resources):
        resources = self.resources

