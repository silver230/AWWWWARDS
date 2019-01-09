from django.test import TestCase
from . models import *
from django.contrib.auth.models import User   

# Create your tests here.
class RatingTestClass(TestCase):
    def setUp(self):
        self.rating=Rating(comment="wooow",design=4,usability= 6, content=7)

    # def tearDown(self) :
    #     Rating.objects.all().delete()

    def test_instance(self):
        self.assertIsInstance(self.rating,Rating)

    def test_save_rating(self):
        self.assertFalse(self.rating in Rating.objects.all())
        self.rating.save()
        self.assertTrue(self.rating in Rating.objects.all())
        self.rating.delete()

    def test_delete_rating(self):
        self.assertFalse(self.rating in Rating.objects.all())
        self.rating.save()
        self.assertTrue(self.rating in Rating.objects.all())
        self.rating.delete()        

class ProjectTestClass(TestCase):
    def setUp(self):
        self.projectTest=Project(name="blog",photo="gifts/media/images/blog.jpg",project_description="a better experience", project_url="https://moringaschool.instructure.com", technologies_used = "html")

    def tearDown(self) :
        User.objects.all().delete()

    def test_instance(self):
        self.assertIsInstance(self.projectTest,Project)

    def test_save_project(self):
        self.assertTrue(self.projectTest in Project.objects.all())
        self.projectTest.save()
         

    def test_delete_project(self):
        self.assertFalse(self.projectTest in Project.objects.all())
        self.projectTest.save()
        self.assertTrue(self.projectTest in Project.objects.all())
        self.projectTest.delete()


