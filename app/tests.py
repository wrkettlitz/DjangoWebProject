"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".
"""

import django
from django.test import TestCase
from app.Friends import *
from app.Forge import *
import sqlite3
import sqlite3
from app.views import *
from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
import unittest
from app.explore import EventHandlerTest
from app.models import PlayerDetails,Player,PlayerTown


from django.http import HttpResponseRedirect    
from django.contrib import auth                 
from django.template.context_processors import csrf 
from django.shortcuts import render_to_response
from app.Town import Town

from app.forms import UserCreationForm
from app.Friends import *
import app.Friends

 

# TODO: Configure your database in settings.py and sync before running tests.

class ViewTest(TestCase):
    """Tests for the application views."""

    if django.VERSION[:2] >= (1, 7):
        # Django 1.7 requires an explicit setup() when running tests in PTVS
        @classmethod
        def setUpClass(cls):
            super(ViewTest, cls).setUpClass()
            django.setup()

    def test_home(self):
        """Tests the home page."""
        response = self.client.get('/')
        self.assertContains(response, 'TownZ', 1, 200)

    def test_contact(self):
        """Tests the contact page."""
        response = self.client.get('/contact')
        self.assertContains(response, 'Contact', 3, 200)

    def test_about(self):
        """Tests the about page."""
        response = self.client.get('/about')
        self.assertContains(response, 'About', 3, 200)





class TownUnittest(TestCase):

    if django.VERSION[:2] >= (1, 7):
        # Django 1.7 requires an explicit setup() when running tests in PTVS
        @classmethod
        def setUpClass(cls):
            super(TownUnittest, cls).setUpClass()
            django.setup()

    #Ja volgensmij moet dit met een setup maar idk
    UnitTest1 = Town.Town("UnitTest1", 20, 3, "Alot", 900, 0, 0,0)
    UnitTest2 = Town.Town("UnitTest2", -20, -3, "Alot", -900, 0, 0,0)
    UnitTest3 = Town.Town("Unit Test 3", 20, 3, "A lot", 900, 0, 0,0)
    UnitTest4 = Town.Town("UnitTest4", 0, 0, "Alot", 0, 0, 0,0)
    UnitTest5 = Town.Town("", 20, 1, "", 900, 0, 0,0)
    UnitTest6 = Town.Town("UnitTest6", -20, -3, "Alot", 900, 0, 0,0)
    UnitTest7 = Town.Town("UnitTest7", 0, 0, "Alot", 900, 4, 0,0)


    def test_Name(self):
        """Test if the towns have the correct name"""
        self.assertEqual(self.UnitTest1.name, "UnitTest1")
        self.assertEqual(self.UnitTest3.name, "Unit Test 3")
        self.assertEqual(self.UnitTest5.name, "")

    def test_Barack(self):
        """Test if baracks can be added correctly"""
        #Just enough money to buy 4
        self.assertEqual(self.UnitTest1.addBarrack(4), 7)

        #But not enough money to buy 5
        self.assertEqual(self.UnitTest1.addBarrack(5), False)

        #Not enough money.
        self.assertEqual(self.UnitTest2.addBarrack(3), False)

        #Not enough money.
        self.assertEqual(self.UnitTest4.addBarrack(1), False)
    
    def test_level(self):
        """Test if the level is correct when buying baracks"""
        #Have no baracks
        self.UnitTest4.addBarrack(0)
        self.assertEqual(self.UnitTest4.level, 0)
        
        #have negative baracks, shouldnt ever happen but test it anyway.
        self.UnitTest2.addBarrack(0)
        self.assertEqual(self.UnitTest2.level, 0)

        #have -3 baracks and add 4 but don't have enough money (-900)
        self.UnitTest2.addBarrack(4)
        self.assertEqual(self.UnitTest2.level, 0)

        #have -3 baracks and add 4 with enough money (900)
        self.UnitTest6.addBarrack(4)
        self.assertEqual(self.UnitTest6.level, 1)

        #have 1 barack
        self.UnitTest5.addBarrack(0)
        self.assertEqual(self.UnitTest5.level, 1)

        #Player is already level 4 and levels up by getting 1 barack
        self.UnitTest7.addBarrack(1)
        self.assertEqual(self.UnitTest7.level, 5)

    def test_money(self):
        """Test if the money is correct when buying baracks"""

        #Enough money to buy 4. 900 - (4*200) = 100
        self.UnitTest1.addBarrack(4)
        self.assertEqual(self.UnitTest1.money, 100)

        #Buying 5 with not enough money. 900 - (5*200) = -100. It should buy as many possible. in this case that would be 4.
        self.UnitTest1.addBarrack(5)
        self.assertEqual(self.UnitTest1.money, 100)

        #Negavite money shouldnt be able to buy anything. Again this shouldnt happen.
        self.UnitTest2.addBarrack(1)
        self.assertEqual(self.UnitTest2.money, -900)

class FriendsUnitTest(TestCase):

    def test_knop(self):
        response = self.client.get('/Friends')
        self.assertContains(response, 'Friends', 5, 200)


class ViewTest(TestCase):
    """Tests for the application views."""
    if django.VERSION[:2] >= (1, 7):
        # Django 1.7 requires an explicit setup() when running tests in PTVS
        @classmethod
        def setUpClass(cls):
            super(ViewTest, cls).setUpClass()
            django.setup()

    def test_home(self):
        """Tests the home page."""
        response = self.client.get('/')
        self.assertContains(response, 'Home Page', 1, 200)

    def test_contact(self):
        """Tests the contact page."""
        response = self.client.get('/contact')
        self.assertContains(response, 'Contact', 3, 200)

    def test_about(self):
        """Tests the about page."""
        response = self.client.get('/about')
        self.assertContains(response, 'About', 3, 200)


# Om te testen, gebruik Command Prompt.
# Command = python manage.py test app.tests.ExploreUnitTest.[functienaam]
# Op een andere manier lukte het niet
class ExploreUnitTest(TestCase):
    if django.VERSION[:2] >= (1, 7):
        # Django 1.7 requires an explicit setup() when running tests in PTVS
        @classmethod
        def setUpClass(cls):
            super(ExploreUnitTest, cls).setUpClass()
            django.setup()
    playerdetails = PlayerDetails.objects.get(pk=1)

    # Geen soldaten gestuurd. Explore fail test
    UnitTest1 = EventHandlerTest.Eventhandler(playerdetails, '', 0, 1, 1, 5, 50, 5)

    # Bandits met 1 soldaat. Explore fail test
    UnitTest2 = EventHandlerTest.Eventhandler(playerdetails, '', 1, 1, 1, 5, 50, 5)

    # Explore succes test
    UnitTest3 = EventHandlerTest.Eventhandler(playerdetails, '', 2, 1, 1, 5, 50, 5)

    # Explore succes. Resources test
    UnitTest4 = EventHandlerTest.Eventhandler(playerdetails, '', 5, 86, 1, 5, 50, 5)

    # Explore 5 soldaten gevonden.
    UnitTest5 = EventHandlerTest.Eventhandler(playerdetails, '', 5, 20, 1, 5, 50, 5)

    # Explore zombies met 1 soldaat
    UnitTest6 = EventHandlerTest.Eventhandler(playerdetails, '', 1, 41, 4, 5, 50, 5)

    # Explore zombies met 5 soldaten
    UnitTest7 = EventHandlerTest.Eventhandler(playerdetails, '', 5, 41, 2, 43, 50, 5)

    # Resources gevonden. Explore succes
    UnitTest8 = EventHandlerTest.Eventhandler(playerdetails, '', 8, 75, 2, 43, 50, 5)

    def ExploreUnitTest1(self):
        self.assertEqual(self.UnitTest1, 'Je hebt het niet gehaald.')

    def ExploreUnitTest2(self):
        self.assertEqual(self.UnitTest2, 'Je hebt het niet gehaald.')

    def ExploreUnitTest3(self):
        self.assertEqual(self.UnitTest3,
                         'Je bent 5 bandits tegengekomen. Je bent tijdens het vuurgevecht 1 soldaten verloren.')

    def ExploreUnitTest4(self):
        self.assertEqual(self.UnitTest4,
                         'Zoektocht geslaagd! Je hebt je eigen dorp weer bereikt met een extra bonus van 50!')

    def ExploreUnitTest5(self):
        self.assertEqual(self.UnitTest5,
                         'Je hebt een klein kamp gevonden met vriendelijke overlevenden. Ze willen graag bij je sluiten. Je hebt 5 soldaten gekregen.')

    def ExploreUnitTest6(self):
        self.assertEqual(self.UnitTest6, 'Je hebt het niet gehaald.')

    def ExploreUnitTest7(self):
        self.assertEqual(self.UnitTest7,
                         'Je bent 43 aantal zombies tegengekomen. Je bent tijdens het gevecht 2 soldaten verloren.')

    def ExploreUnitTest8(self):
        self.assertEqual(self.UnitTest8,
                         'Je bent een vervallen gebouw tegenkomen. Uit dit gebouw heb je 50 resources kunnen halen.')


class Testing(unittest.TestCase):
    SoldierUnitTest2 = Town.Town("UnitTest2", -20, -3, "Alot", -900, -10,-900,-10)
    SoldierUnitTest3 = Town.Town("UnitTest3", 20, 3, "Alot", 400, 3,400,3)
    SoldierUnitTest4 = Town.Town("UnitTest4", 0, 0, "Alot", 1000, 0,1000,0)
    SoldierUnitTest5 = Town.Town("UnitTest5", 20, 3, "Alot", 900, -5,900,-5)
    
    

    def test_soldier(self):
        # Not enough money
        self.assertEqual(self.SoldierUnitTest2.addSoldier(2), False)

        self.assertEqual(self.SoldierUnitTest3.addSoldier(2), 5)

        self.assertEqual(self.SoldierUnitTest5.addSoldier(4), -1)

    def test_money(self):
        self.SoldierUnitTest4.addSoldier(1)
        self.assertEqual(self.SoldierUnitTest4.money, 900)


class Test2(unittest.TestCase):
    UnitTest6 = Town.Town("UnitTest6", 20, 3, "Alot", 200, 0,0,200)
    UnitTest7 = Town.Town("UnitTest7", 5, 5, "Alot", 100, 4,100,4)
    UnitTest8 = Town.Town("UnitTest8", 2, 6, "Alot", 700, 3,700,3)
    UnitTest9 = Town.Town("UnitTest9", 3, 7, "Alot", 800, 0,800,0)
    UnitTest10 = Town.Town("UnitTest10", 2, 9, "Alot", 600, 2,600,2)
    UnitTest11 = Town.Town("UnitTest11", 4, 7, "Alot", 700, 10,700,10)

    def TownUnitTest6(self):
        self.assertEqual(self.UnitTest6.addSoldier(1),
                         "Soldier were created. The soldier fights a horde of zombies and dies")

    def TownUnitTest7(self):
        self.assertEqual(self.UnitTest6.addSoldier(2),
                         "6 Soldiers were created.The soldiers were crushed by a big titan.")

    def TownUnitTest8(self):
        self.assertEqual(self.UnitTest8.addSoldier(5),
                         "8 Soldiers were created. The soldiers killed the titan, but got killed by the gravekeeper.")

    def TownUnitTest9(self):
        self.assertEqual(self.UnitTest9.addSoldier(9),
                         "9 Soldiers were created. The soldiers killed the zombies and the titan, but got killed by an exploding bomb.")

    def TownUnitTest10(self):
        self.assertEqual(self.UnitTest10.addSoldier(1),
                         "3 Soldiers were created. The soldiers went into a graveyard and got buried alive by the gravekeeper.")

    def TownUnitTest11(self):
        self.assertEqual(self.UnitTest10.addSoldier(0),
                         "10 Soldiers were created. The soldiers killed the bandits, zombies, titan, gravekeeper and the unknown entity. Congratulations! Go to the next level!")



class ForgeTest(unittest.TestCase):
    #We gaan de Admin Account (ID 2) Gebruiken voor deze test.
    #hiermee kunnen we de values zetten die we gebruiken voor de test.
    Set = Forge.TestAccountDefaultValues
    #Omdat we de object "request.user.id" gebruiken in Forge moet request.user.id 2 zijn.
    request = type('', (), {})()
    request.user = type('', (), {})()
    request.user.id =2


    def test(self):

            
            #nu geven we de admin account een level 1 wapen en 10000 credits
            self.Set(2,1,10000)
            #nu kopen we een level 2 wapen.
            Forge.BuyWeapon(self.request, 10000, 2500, 1)
            #Nu moet de admin een level 2 wapen hebben en 7500 credits.
            self.assertEqual(int(Forge(self.request).current_weapon_level), 2)
            self.assertEqual(int(Forge(self.request).Credits), 7500)
    def test2(self):

            #nu level 3 wapen.
            self.Set(2,2,7500)
            Forge.BuyWeapon(self.request, 7500, 5000, 2)
            #Nu moet de admin een level 3 wapen hebben en 2500 credits.
            self.assertEqual(int(Forge(self.request).current_weapon_level), 3)
            self.assertEqual(int(Forge(self.request).Credits), 2500)
    def test3(self):
            #nu level 4 met onvoldoende geld
            self.Set(2,3,2500)
            Forge.BuyWeapon(self.request, 2500, 10000, 3)
            #Nu moet de admin een level 3 wapen hebben en 2500 credits.
            self.assertEqual(int(Forge(self.request).current_weapon_level), 3)
            self.assertEqual(int(Forge(self.request).Credits), 2500)
    def test4(self):        

            #nu level 4 met voldoende geld
            self.Set(2,3,20000)
            Forge.BuyWeapon(self.request, 20000, 10000, 3)
            #Nu moet de admin een level 4 wapen hebben en 10000 credits.
            self.assertEqual(int(Forge(self.request).current_weapon_level), 4)
            self.assertEqual(int(Forge(self.request).Credits), 10000)
    def test5(self):
            
            #nu level 5 maar level 5 bestaat niet
            self.Set(2,4,20000)
            Forge.BuyWeapon(self.request, 500, 10000, 4)
            #Nu moet de admin een level 4 wapen hebben en 20000 credits.
            self.assertEqual(int(Forge(self.request).current_weapon_level), 4)
            self.assertEqual(int(Forge(self.request).Credits), 20000)

            
    def test6(self):
        #backtodefault
        self.Set(2,1,10000)
        self.assertEqual(int(Forge(self.request).current_weapon_level), 1)
        self.assertEqual(int(Forge(self.request).Credits), 10000)
        
       

            






