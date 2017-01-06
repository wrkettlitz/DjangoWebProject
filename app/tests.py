"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".
"""

import django
from django.test import TestCase
from app.Friends import *
import sqlite3
import sqlite3
from app.views import *
from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime



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
    UnitTest1 = Town("UnitTest1", 20, 3, "Alot", 900, 0, 0)
    UnitTest2 = Town("UnitTest2", -20, -3, "Alot", -900, 0, 0)
    UnitTest3 = Town("Unit Test 3", 20, 3, "A lot", 900, 0, 0)
    UnitTest4 = Town("UnitTest4", 0, 0, "Alot", 0, 0, 0)
    UnitTest5 = Town("", 20, 1, "", 900, 0, 0)
    UnitTest6 = Town("UnitTest6", -20, -3, "Alot", 900, 0, 0)
    UnitTest7 = Town("UnitTest7", 0, 0, "Alot", 900, 4, 0)


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