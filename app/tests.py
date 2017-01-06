"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".
"""

import django
from django.test import TestCase
from app.explore import EventHandlerTest
from app.models import PlayerDetails

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

    #Geen soldaten gestuurd. Explore fail test
    UnitTest1 = EventHandlerTest.Eventhandler(playerdetails,'',0,1,1,5,50,5)

    #Bandits met 1 soldaat. Explore fail test
    UnitTest2 = EventHandlerTest.Eventhandler(playerdetails,'',1,1,1,5,50,5)

    #Explore succes test
    UnitTest3 = EventHandlerTest.Eventhandler(playerdetails,'',2,1,1,5,50,5)

    #Explore succes. Resources test
    UnitTest4 = EventHandlerTest.Eventhandler(playerdetails,'',5,86,1,5,50,5)

    #Explore 5 soldaten gevonden.
    UnitTest5 = EventHandlerTest.Eventhandler(playerdetails,'',5,20,1,5,50,5)

    #Explore zombies met 1 soldaat
    UnitTest6 = EventHandlerTest.Eventhandler(playerdetails,'',1,41,4,5,50,5)

    #Explore zombies met 5 soldaten
    UnitTest7 = EventHandlerTest.Eventhandler(playerdetails,'',5,41,2,43,50,5)

    #Resources gevonden. Explore succes
    UnitTest8 = EventHandlerTest.Eventhandler(playerdetails,'',8,75,2,43,50,5)


    def ExploreUnitTest1(self):
        self.assertEqual(self.UnitTest1,'Je hebt het niet gehaald.')
        
    def ExploreUnitTest2(self):
        self.assertEqual(self.UnitTest2,'Je hebt het niet gehaald.')

    def ExploreUnitTest3(self):
        self.assertEqual(self.UnitTest3,'Je bent 5 bandits tegengekomen. Je bent tijdens het vuurgevecht 1 soldaten verloren.')

    def ExploreUnitTest4(self):
        self.assertEqual(self.UnitTest4,'Zoektocht geslaagd! Je hebt je eigen dorp weer bereikt met een extra bonus van 50!')

    def ExploreUnitTest5(self):
        self.assertEqual(self.UnitTest5,'Je hebt een klein kamp gevonden met vriendelijke overlevenden. Ze willen graag bij je sluiten. Je hebt 5 soldaten gekregen.')

    def ExploreUnitTest6(self):
        self.assertEqual(self.UnitTest6,'Je hebt het niet gehaald.')

    def ExploreUnitTest7(self):
        self.assertEqual(self.UnitTest7,'Je bent 43 aantal zombies tegengekomen. Je bent tijdens het gevecht 2 soldaten verloren.')

    def ExploreUnitTest8(self):
        self.assertEqual(self.UnitTest8,'Je bent een vervallen gebouw tegenkomen. Uit dit gebouw heb je 50 resources kunnen halen.')

       



