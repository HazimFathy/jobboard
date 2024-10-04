from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

# signup form
class signupform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
   
#user form
class UserForm(forms.ModelForm):
    class Meta:
        model= User
        fields=['first_name','last_name','email']
   
#profile form     
class profileform(forms.ModelForm):
    class Meta:
        model = Profile
        fields='__all__'
        exclude=('user',)


