from django import forms
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Project,Profile,Review

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project 
        exclude =['user', 'profile']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user_nam e', 'bio']     