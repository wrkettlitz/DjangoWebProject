"""
Definition of urls for TownZVisual.
"""

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

# Uncomment the next lines to enable the admin:\


urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^story', app.views.TownZ, name='TownZ'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^result', app.views.Result, name='result'),
    url(r'^explore', include('app.urls')),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about', app.views.about, name='about'),
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

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

]
