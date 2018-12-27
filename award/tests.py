from django.test import TestCase
from . models import Project        

# Create your tests here.
class ProjectTestClass(TestCase):
    def setUp(self):
        self.projectTest=Project(name="blog",photo="gifts/media/images/blog.jpg",project_description="a better experience", project_url="https://moringaschool.instructure.com", technologies_used = "html")

    # def tearDown(self) :
    #     User.objects.all().delete()

    def test_instance(self):
        self.assertIsInstance(self.projectTest,Project)

    def test_save_project(self):
        self.assertFalse(self.projectTest in Project.objects.all())
        self.projectTest.save()
        self.assertTrue(self.projectTest in Project.objects.all())
        self.projectTest.delete()

    def test_delete_project(self):
        self.assertFalse(self.projectTest in Project.objects.all())
        self.projectTest.save()
        self.assertTrue(self.projectTest in Project.objects.all())
        self.projectTest.delete()