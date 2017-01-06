"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from .models import Player, PlayerDetails,PlayerTown
from .forms import ExploreForm,Town
from .explore import *

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
    context = {'playerrecources':ExploreForm.playerrecourses, 'playersoldiers': ExploreForm.playersoldiers, "form":form_class, 'title':'TownZ'}
    assert isinstance(request, HttpRequest)
    return render(request, 'app/explore.html', context)


    
def Result(request):
    gekozen_aantal = request.POST["exploreform"]
    explorehand = EventHandler()
    playerdetails = PlayerDetails.objects.get(id=1)
    Eindresultaat = ''
    Eindresultaat = explorehand.Eventhandler(playerdetails,Eindresultaat,gekozen_aantal)
    context = {'end' : Eindresultaat }
    return render(request , 'app/result.html', context)


def TownZ(request):
    townform = Town()
    context = {'title':'TownZ','message':'Your level page.', 'form':townform.playerrescources}
    assert isinstance(request, HttpRequest)
    return render(request,'app/townZ.html', context)
