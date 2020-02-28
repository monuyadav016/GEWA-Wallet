from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):

    class Meta():
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['first_name'].widget.attrs.update({'autofocus': ''})
        self.fields['username'].label = 'Username'
        self.fields['username'].widget.attrs.update({'input_type': 'email'})
        self.fields['first_name'].label = 'First Name'
        self.fields['first_name'].required = True
        self.fields['last_name'].label = 'Last Name'
        self.fields['email'].label = 'Confirm Email Address'
        self.fields['email'].required = True
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Confirm Password'