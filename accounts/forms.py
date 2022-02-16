from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms


class CustomUserCreationForm(UserCreationForm):
    """
    A Custom form for creating new users.
    """
    password1 = forms.CharField(label='Password', widget = forms.PasswordInput(attrs = {'class': 'form-control','id': 'pass','placeholder': 'Atleast 8 charecters minimum. Alphanumaric and a special'}))
    password2 = forms.CharField(label='Confirm Password', widget = forms.PasswordInput(attrs = {'class': 'form-control','id': 'cpass','placeholder': 'Re-type it for confirmation'}))

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'user_name', 'email', 'password1', 'password2']
        label = { 'first_name':'First Name', 'last_name':'Last Name', 'username':'Username', 'email':'Email' }
        widgets ={
        'first_name':forms.TextInput(attrs = {'class': 'form-control','id': 'fname','placeholder': 'Jhon'}),
        'last_name':forms.TextInput(attrs = {'class': 'form-control','id': 'Lname','placeholder': 'Andrew'}),
        'user_name':forms.TextInput(attrs = {'class': 'form-control','id': 'username','placeholder': 'xyz'}),
        'email':forms.EmailInput(attrs = {'class': 'form-control','id': 'email-id','placeholder': 'xyz@example.com'}),
        }

class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'DOB', 'university', 'branch', 'specitalization', 'bio', 'status', 'endyear', 'phone']

        widgets = {
        'first_name':forms.TextInput(attrs = {'class': 'form-control','id': 'fnameu','placeholder': 'Jhon'}),
        'last_name':forms.TextInput(attrs = {'class': 'form-control','id': 'Lnameu','placeholder': 'Andrew'}),
        'email':forms.EmailInput(attrs = {'class': 'form-control','id': 'email-id','placeholder': 'xyz@example.com'}),
        'DOB':forms.NumberInput(attrs={'class': 'form-control','type': 'date','id':'dob'}),
        'university':forms.TextInput(attrs = {'class': 'form-control','id': 'university','placeholder': 'xyz university'}),
        'branch':forms.TextInput(attrs = {'class': 'form-control','id': 'branch','placeholder': 'branch'}),
        'specitalization':forms.TextInput(attrs = {'class': 'form-control','id': 'specitalization','placeholder': 'specitalization'}),
        'bio':forms.Textarea(attrs = {'class': 'form-control','id': 'bio','placeholder': 'bio'}),
        'status':forms.Select(attrs = {'class': 'form-control','id': 'status','placeholder': 'status'}),
        'endyear':forms.NumberInput(attrs={'class': 'form-control','type': 'year','id':'endyear'}),
        'phone':forms.NumberInput(attrs={'class': 'form-control','type': 'phonenumber_field','id':'phone'}),
        }
