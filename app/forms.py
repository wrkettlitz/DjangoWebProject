"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Player,PlayerTown,PlayerDetails

 

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


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.TextInput({'class': 'form-control', 'placeholder': 'E-mail'}))
    username = forms.CharField(required=True, widget=forms.TextInput({'class': 'form-control', 'placeholder': 'User name'}))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput({'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput({'class': 'form-control', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.username = self.cleaned_data["username"]
        if commit:
            user.save()
        return user
class ExploreForm(forms.Form):
    playerdetails = PlayerDetails.objects.get(id=1)
    playerrecourses = playerdetails.Resources
    playersoldiers = playerdetails.Soldiers
    exploreform = forms.IntegerField(max_value=playersoldiers,min_value=1)

class TownForm(forms.Form):
    playerdetails = PlayerDetails.objects.get(pk=1)
    playerTown = PlayerTown.objects.get(id=playerdetails.id)
    playerrescources = playerdetails.Resources
    playerbarrack = playerTown.BarrackName
    Player = Player.objects.get(id=1)
    Money = playerTown.Money
    BarrackName = playerTown.BarrackName
    PlayerSoldier = playerdetails.Soldiers
    townform = forms.Textarea()