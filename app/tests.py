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
        self.assertContains(response, 'Home Page', 1, 200)

    def test_contact(self):
        """Tests the contact page."""
        response = self.client.get('/contact')
        self.assertContains(response, 'Contact', 3, 200)

    def test_about(self):
        """Tests the about page."""
        response = self.client.get('/about')
        self.assertContains(response, 'About', 3, 200)

        from django.test import TestCase


class FriendsUnitTest(TestCase):

    def test_knop(self):
        response = self.client.get('/Friends')
        self.assertContains(response, 'Friends', 5, 200)