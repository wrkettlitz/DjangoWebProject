"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from . import Explore
from . import Town
from . import player



from django.http import HttpResponseRedirect    
from django.http import HttpResponse
from django.contrib import auth                 
from django.template.context_processors import csrf 
from django.shortcuts import render_to_response

from app.forms import UserCreationForm


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
    currenstats = Explore.CurrentStats
    
    """Renders the explore page."""
    assert isinstance(request, HttpRequest)   
    return render(
        request,
        'app/explore.html',
        {
            'title':'Explore',
            'message': currenstats.CurrentSoldiers(100) ,
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






