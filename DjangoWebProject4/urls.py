"""
Definition of urls for DjangoWebProject4.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views
import app.forms
import app.views
from datetime import datetime
from django.conf.urls import url, include
from app.models import Player,PlayerDetails,PlayerTown
import django.contrib.auth.views
from django.contrib import admin
import app.forms
import app.views
admin.autodiscover()

admin.site.register(Player)
admin.site.register(PlayerDetails)
admin.site.register(PlayerTown)


# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^Friends', app.views.friends, name='Friends'),
    url(r'^about', app.views.about, name='about'),
    url(r'^explore', include('app.urls')),
    url(r'^result', app.views.Result, name='result'),
    url(r'^City', app.views.Barack, name='City'),
    url(r'^TownZ', app.views.TownZ, name='TownZ'),
    url(r'^Page2', app.views.Page2, name='Page2'),


    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    url(r'^register$', 
        app.views.register_user, 

        
        name='register', ),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
]
