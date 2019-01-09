from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Project,Rating

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project 
        exclude =['user', 'profile',]
        # fields = ('name','photo','projects_url')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email')
        
# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields =( 'user','bio')    

class RatingForm(forms.ModelForm):
    class Meta:
        model=Rating
        exclude = ['profile','project']   