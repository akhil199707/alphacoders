from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from django.forms import ModelForm


class AnswerForm(forms.Form):
    
    Code = forms.CharField(widget=forms.Textarea(attrs = {'class': 'form-control','id': 'code','placeholder': 'Code'}))
