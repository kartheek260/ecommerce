import django
from django import forms

from .models import registers


class RegForm(django.forms.ModelForm):
    class Meta:
        model = registers
        widgets = {'Password': django.forms.PasswordInput(), 'confirm_Password': django.forms.PasswordInput()}
        fields = ['first_name','last_name','email','Password','confirm_Password','phone']


class LoginForm(django.forms.Form):
    email = forms.EmailField()
    Password = forms.CharField(widget=forms.PasswordInput())