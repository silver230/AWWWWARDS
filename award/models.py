from django.db import models
from django.contrib.auth.models import User
import datetime as dt
 

# Create your models here.

class Profile (models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    username = models.CharField(max_length= 70)
    bio = models.CharField(max_length=60),
    date_of_birth = models.TimeField(max_length=30),
    
    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()
   

    def __str__(self):
        return self.username
