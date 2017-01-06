from .forms import Player,PlayerDetails
import random

class EventHandlerTest():
    @staticmethod
    def Eventhandler(playerdetails,end,gekozen_aantal,randomint,lost,tegen,Recources,Soldiers):
        e = ExploreFunctionTest()
        if playerdetails.Soldiers == 0 or gekozen_aantal == 0 :
            end = str(e.ExploreFailed(playerdetails,end,gekozen_aantal))
        elif (playerdetails.Soldiers < gekozen_aantal):
              gekozen_aantal = playerdetails.Soldiers
        else:
            if randomint > 85:
                end = str(e.ExploreSucces(playerdetails,end,gekozen_aantal,Recources))
            if randomint > 0 and randomint < 20:
                end = str(e.Bandits(playerdetails,end,gekozen_aantal,lost,tegen))
            if randomint > 19 and randomint < 40:
                end = str(e.GainedSoldiers(playerdetails,end,gekozen_aantal,Soldiers))
            if randomint >= 40 and randomint < 70:
                end = str(e.Zombies(playerdetails,end,gekozen_aantal,lost,tegen))
            if randomint > 70 and randomint <= 85:
                end = str(e.GainedResources(playerdetails,end,gekozen_aantal,Recources))
            if (gekozen_aantal == 0):
                end = str(e.ExploreFailed(playerdetails,end,gekozen_aantal))
        return str(end)

class ExploreFunctionTest():
    @staticmethod
    def Bandits(playerdetails,end,gekozen_aantal,lost,tegen):
        e = ExploreFunctionTest()
        if lost > gekozen_aantal:
            lost = gekozen_aantal
        playerdetails.Soldiers = playerdetails.Soldiers - lost
        gekozen_aantal = gekozen_aantal - lost
        if gekozen_aantal > 0:
            end = end + 'Je bent ' + str(tegen) + ' bandits tegengekomen. Je bent tijdens het vuurgevecht '+ str(
                    lost) + ' soldaten verloren.'
            return end
        else:
            end = str(e.ExploreFailed(playerdetails,end,gekozen_aantal))
            return end

    @staticmethod
    def Zombies(playerdetails,end,gekozen_aantal,lost, tegen):
        e = ExploreFunctionTest()
        if lost > gekozen_aantal:
            lost = gekozen_aantal
        playerdetails.Soldiers = playerdetails.Soldiers - lost
        gekozen_aantal = gekozen_aantal - lost
        if gekozen_aantal > 0:
            end = end + 'Je bent ' + str(tegen) + ' aantal zombies tegengekomen. Je bent tijdens het gevecht '+ str(
            lost) + ' soldaten verloren.'
            return end
        else:
            end = str(e.ExploreFailed(playerdetails,end,gekozen_aantal))
            return end

    @staticmethod
    def GainedResources(playerdetails,end,gekozen_aantal,Resources):
        playerdetails.Resources = playerdetails.Resources + Resources
        end = end + 'Je bent een vervallen gebouw tegenkomen. Uit dit gebouw heb je ' + str(Resources) +' resources kunnen halen.'
        return end

    @staticmethod
    def GainedSoldiers(playerdetails,end,gekozen_aantal,Soldiers):
        playerdetails.Soldiers = playerdetails.Soldiers + Soldiers
        return 'Je hebt een klein kamp gevonden met vriendelijke overlevenden. Ze willen graag bij je sluiten. Je hebt '+  str(Soldiers) + ' soldaten gekregen.'

    @staticmethod
    def ExploreSucces(playerdetails,end,gekozen_aantal,Resources):
        playerdetails.Resources = playerdetails.Resources + Resources
        return 'Zoektocht geslaagd! Je hebt je eigen dorp weer bereikt met een extra bonus van '+ str(Resources) + '!'

    @staticmethod
    def ExploreFailed(playerdetails,end,gekozen_aantal):
        return 'Je hebt het niet gehaald.'
        










class EventHandler():
    @staticmethod
    def Eventhandler(playerdetails,end,gekozen_aantal):
        e = ExploreFunction()
        gekozen_aantal = int(gekozen_aantal)
        if playerdetails.Soldiers ==0 :
            e.ExploreFailed(playerdetails,end,gekozen_aantal)
        elif (playerdetails.Soldiers < gekozen_aantal):
              gekozen_aantal = playerdetails.Soldiers
        else:
            randomint = random.randint(0,100)
            if randomint > 85:
                end = e.ExploreSucces(playerdetails,end,gekozen_aantal)
            if randomint > 0 and randomint < 20:
                end = str(e.Bandits(playerdetails,end,gekozen_aantal))
            if randomint > 19 and randomint < 40:
                end = str(e.GainedSoldiers(playerdetails,end,gekozen_aantal))
            if randomint >= 40 and randomint < 70:
                end = str(e.Zombies(playerdetails,end,gekozen_aantal))
            if randomint > 70 and randomint <= 85:
                end = str(e.GainedResources(playerdetails,end,gekozen_aantal))
            if (gekozen_aantal == 0):
                end = str(e.ExploreFailed(playerdetails,end,gekozen_aantal))
        return end

class ExploreFunction():
    @staticmethod
    def Bandits(playerdetails,end,gekozen_aantal):
        e = ExploreFunction()
        lost = random.randint(1,4)
        if lost > gekozen_aantal:
            lost = gekozen_aantal
        playerdetails.Soldiers = playerdetails.Soldiers - lost
        gekozen_aantal = gekozen_aantal - lost
        if gekozen_aantal > 0:
            end = end + 'Je bent ' + str(random.randint(5,10)
                                         ) + ' bandits tegengekomen. \n' + 'Je bent tijdens het vuurgevecht '+ str(
                    lost) + ' soldaten verloren.\n' + 'Je hebt ' + str(lost)+ ' soldaten over.'
            playerdetails.save()
            return end
        else:
            playerdetails.save()
            end = str(e.ExploreFailed(playerdetails,end,gekozen_aantal))
            return end

    @staticmethod
    def Zombies(playerdetails,end,gekozen_aantal):
        e = ExploreFunction()
        lost = random.randint(0,10)
        if lost > gekozen_aantal:
            lost = gekozen_aantal
        playerdetails.Soldiers = playerdetails.Soldiers - lost
        gekozen_aantal = gekozen_aantal - lost
        if gekozen_aantal > 0:
            end = end + 'Je bent ' + str(random.randint(
            10,50)) + ' aantal zombies tegengekomen. \n' + 'Je bent tijdens het gevecht '+ str(
            lost) + ' soldaten verloren.\n'
            playerdetails.save()
            return end
        else:
            playerdetails.save()
            end = str(e.ExploreFailed(playerdetails,end,gekozen_aantal))
            return end

    @staticmethod
    def GainedResources(playerdetails,end,gekozen_aantal):
        Resources = random.randint(30,80)
        playerdetails.Resources = playerdetails.Resources + Resources
        playerdetails.save()
        end = end + 'Je bent een vervallen gebouw tegenkomen. Uit dit gebouw heb je ' + str(Resources) +' resources kunnen halen'
        return end

    @staticmethod
    def GainedSoldiers(playerdetails,end,gekozen_aantal):
        Soldiers = random.randint(2,10)
        playerdetails.Soldiers = playerdetails.Soldiers + Soldiers
        end = end + 'Je hebt een klein kamp gevonden met vriendelijke overlevenden. Ze willen graag bij je sluiten. Je hebt '+  str(Soldiers) + ' soldaten gekregen.'
        playerdetails.save()
        return end

    @staticmethod
    def ExploreSucces(playerdetails,end,gekozen_aantal):
        Resources = random.randint(50,100)
        playerdetails.Resources = playerdetails.Resources + Resources
        playerdetails.save()
        end = end + 'Zoektocht geslaagd! Je hebt je eigen dorp weer bereikt met een extra bonus van '+ str(Resources) + '! '
        return end

    @staticmethod
    def ExploreFailed(playerdetails,end,gekozen_aantal):
        playerdetails.save()
        end = end + 'Je hebt het niet gehaald. Er was geen enkele soldaat die de zoektocht overleefd heeft. :('
        return end