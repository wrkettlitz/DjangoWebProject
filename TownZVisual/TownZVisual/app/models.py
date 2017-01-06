from django.db import models

class Player(models.Model):
    PlayerName = models.CharField(max_length=50)
    Level = models.IntegerField()

    def __str__(self):
        return 'Player name: ' + self.PlayerName + '. Player level: ' + str(self.Level)


class PlayerDetails(models.Model):
    Player_id = models.ForeignKey(Player, on_delete=models.CASCADE)
    Resources = models.IntegerField()
    Soldiers = models.IntegerField()

    def __str__(self):
        return str(self.Player_id) + '. Player resources: ' + \
               str(self.Resources) + '. Player soldiers: ' + str(self.Soldiers)

class PlayerTown(models.Model):
    Town_id = models.ForeignKey(Player, on_delete=models.CASCADE)
    Money = models.IntegerField()
    BarrackName = models.CharField(max_length=50)
    

