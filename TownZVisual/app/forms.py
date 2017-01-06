from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from .models import Player,PlayerDetails,PlayerTown

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class ExploreForm(forms.Form):
    playerdetails = PlayerDetails.objects.get(id=1)
    playerrecourses = playerdetails.Resources
    playersoldiers = playerdetails.Soldiers
    exploreform = forms.IntegerField(max_value=playersoldiers,min_value=1)

class Town(forms.Form):
    playerdetails = PlayerDetails.objects.get(pk=1)
    playerTown = PlayerTown.objects.get(id=playerdetails.id)
    playerrescources = playerdetails.Resources
    playerbarrack = playerTown.BarrackName
    townform = forms.Textarea()
