from django.test import TestCase
from foodive import *
from foodive.models import User


class TestAppModels(TestCase):

    def test_model_str(self):
        user = User.objects.create(name="Hola")
        user2 = User.objects.create(location="Some location")

        self.assertEqual(str(user), "Hola")
        #assumes that the User object has a name Hola
        self.assertEqual(str(user2), "Some location")
        #assumes that the User object has a location "Some Location"
