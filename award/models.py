from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Profile (models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True),
    user_name = models.CharField(max_length= 70),
    bio = models.CharField(max_length=60),


    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()


    def __str__(self):
        return self.user_name

