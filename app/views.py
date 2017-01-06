"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from . import explore
from . import Town
from . import player
from . import Town
from .forms import ExploreForm,TownForm

from .models import Player, PlayerDetails,PlayerTown
from .forms import ExploreForm
from .explore import *
from django.http import HttpResponseRedirect    
from django.http import HttpResponse
from django.contrib import auth                 
from django.template.context_processors import csrf 
from django.shortcuts import render_to_response

from app.forms import UserCreationForm
from app.Friends import *
import app.Friends
"""Activates sqlite3, IMPORTANT! ;)"""

#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('db.sqlite3')

print("Opened database successfully");


"""This is a test, NOT important"""


print("Testing DataBase");
conn.execute("""DROP TABLE IF EXISTS COMPANY """)
conn.execute('''CREATE TABLE COMPANY
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL);''')
print("Table created successfully");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 )");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");

conn.commit()
print("Records created successfully");

cursor = conn.execute("SELECT id, name, address, salary  from COMPANY")
for row in cursor:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("ADDRESS = ", row[2])
   print("SALARY = ", row[3], "\n")

print("Operation done successfully");


""" end test"""


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )


def explore(request):
    form_class = ExploreForm()
    context = {'playerrecources': ExploreForm.playerrecourses, 'playersoldiers': ExploreForm.playersoldiers,
               "form": form_class, 'title': 'TownZ'}
    assert isinstance(request, HttpRequest)
    return render(request, 'app/explore.html', context)


def Result(request):
    gekozen_aantal = request.POST["exploreform"]
    explorehand = EventHandler()
    playerdetails = PlayerDetails.objects.get(id=1)
    Eindresultaat = ''
    Eindresultaat = explorehand.Eventhandler(playerdetails, Eindresultaat, gekozen_aantal)
    context = {'end': Eindresultaat}
    return render(request, 'app/result.html', context)

def friends(request):
    """Renders the Friends list."""
    assert isinstance(request, HttpRequest)
    current_user = request.user
    Friends= app.Friends.Friends
    if request.user.is_authenticated():
        return render(
            request,
            'app/Friends.html',
            {
                'title':'Friends',
                'message':'Your Friends list.',
                'Friend_list':Friends(request).Friend_list_name,

                'year':datetime.now().year,
            }
            )
    else:
        return render(
            request,
            'app/Friends.html',
            {
                'title':'Friends',
                'message':'Your Friends list.',
                'Friend_list':"Please log in",

                'year':datetime.now().year,
            }
            )

def register_user(request):
    """Registers users"""
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            saved_email = request.POST.get("email", "")
            saved_username = request.POST.get("username", "")
            saved_password1 = request.POST.get("password1", "")
            saved_password2 = request.POST.get("password2", "")
            form.save()
            return HttpResponseRedirect('/')

    args = {}
    args.update(csrf(request))

    args['form'] = UserCreationForm()

    return render_to_response('app/register.html', args)


def Barack(request):
    Baracks = Town.Town
    
    """Renders the explore page."""
    assert isinstance(request, HttpRequest)  

    if request.method =='POST':
        if Town.T.addBarrack(1) == False:
            return render(
                request,
                'app/City.html',
                {
                    'title':'Amount of baracks:',
                    'Barracks': Town.T.amount_of_barracks,
                    'Money': Town.T.money,
                    'error': 'Not enough money to buy',
                    'level': Town.T.level,
                }
            )
    return render(
    request,
    'app/City.html',
    {
        'title':'Amount of baracks:',
        'Barracks': Town.T.amount_of_barracks,
        'Money': Town.T.money,
        'level': Town.T.level,
    }
)


def TownZ(request):
    townform = TownForm()
    context = {'title':TownZ,'Player': townform.Player.PlayerName,'PlayerSoldier': townform.playerdetails.Soldiers,'BarrackName': townform.playerTown.BarrackName}
    assert isinstance(request, HttpRequest)
    return render(request,'app/townZ.html', context)

def Page2(request):
    townform = TownForm()


    assert isinstance(request, HttpRequest)
    if request.method=='POST':
        Town.T.addSoldier(1)

        if Town.T.amount_of_soldiers == 1:
            text = "Soldier were created. The soldier fights a horde of zombies and dies."
        elif Town.T.amount_of_soldiers == 2:
            text = "2 Soldiers were created. The soldiers were killed by bandits"
        elif Town.T.amount_of_soldiers == 3:
            text = "3 Soldiers were created. The soldiers went into a graveyard and got buried alive by the gravekeeper."
        elif Town.T.amount_of_soldiers == 4:
            text = "4 Soldier were created. The soldiers went into a castle and got killed by an unknown entity."
        elif Town.T.amount_of_soldiers == 5:
            text = "5 Soldiers were created. The soldiers fell into a cave...they died"
        elif Town.T.amount_of_soldiers == 6:
            text = " 6 Soldiers were created.The soldiers were crushed by a big titan"
        elif Town.T.amount_of_soldiers == 7:
            text = "7 Soldiers were created. The soldiers killed a horde of zombies, but they got infected and died."
        elif Town.T.amount_of_soldiers == 8:
            text = "8 Soldiers were created. The soldiers killed the titan, but got killed by the gravekeeper"
        elif Town.T.amount_of_soldiers == 9:
            text = "9 Soldiers were created. The soldiers killed the zombies and the titan, but got killed by an exploding bomb."
        elif Town.T.amount_of_soldiers == 10:
            text = "10 Soldiers were created. The soldiers killed the bandits, zombies, titan, gravekeeper and the unknown entity. Congratulations! Go to the next level!"
        else:
            text = str(Town.T.amount_of_soldiers) + "Soldiers were created"

    context = {'Player': Town.T.name, 'PlayerSoldier': Town.T.amount_of_soldiers, 'Money': Town.T.money,'Player2': townform.Player.PlayerName, 'text': text}


    return render(request, 'app/Page2.html', context)





