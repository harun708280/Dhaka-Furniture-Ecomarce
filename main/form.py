from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField

class RegistrationForm(UserCreationForm):
    class Meta:       
        model=User
        fields=['username','first_name','last_name','email','password1','password2']

class LoginForm(AuthenticationForm):
    class Meta:
        
        fields=['username','password']        

class CouponForm(forms.Form):
    code =forms.CharField()