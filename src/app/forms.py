from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Adonator

class AdonatorCreationForm(UserCreationForm):

    class Meta:
        model = Adonator
        fields = ('username', 'email', 'password')

class AdonatorChangeForm(UserChangeForm):

    class Meta:
        model = Adonator
        fields = UserChangeForm.Meta.fields