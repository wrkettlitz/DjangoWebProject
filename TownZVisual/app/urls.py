from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views
import app.forms
import app.views
from . import views

urlpatterns = [
    url(r'^$',views.explore, name='explore'),
    ]
