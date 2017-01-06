"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime



from django.http import HttpResponseRedirect    
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

def register_user(request):
    """Registers users"""
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():

            form.save()
            return HttpResponseRedirect('/')

    args = {}
    args.update(csrf(request))

    args['form'] = UserCreationForm()

    return render_to_response('app/register.html', args)




