from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Profile (models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True),
    username = models.CharField(max_length= 70),
    bio = models.CharField(max_length=60),
    profile_pic = models.ImageField(upload_to='media/', blank=True)

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

class Project(models.Model):

    name = models.CharField(max_length=30),
    photo =  models.CharField(max_length=50),
    project_description = models.CharField(max_length=50),
    project_url = models.CharField(max_length=50),
    technologies_used = models.CharField(max_length=50),
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True),
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True),
    posted_time = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-posted_time']

    def __str__(self):
        return self.name

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    @classmethod
    def get_project(cls):
        projects = cls.objects.all()
        return projects

    @classmethod
    def filter_by_search_term(cls, search_term):
        return cls.objects.filter(name__icontains=search_term)    

class Rating(models.Model):
    design = models.IntegerField(blank=True,default=0)
    usability = models.IntegerField(blank=True,default=0)
    creativity = models.IntegerField(blank=True,default=0)
    content = models.IntegerField(blank=True,default=0)
    overall_score = models.IntegerField(blank=True,default=0)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
