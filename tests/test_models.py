from django.test import TestCase
from foodive import *
from foodive.models import User


class TestAppModels(TestCase):

    def test_model_str(self):
        user = User.objects.create(name="Hola")
        user2 = User.objects.create(location="Some location")

        self.assertEqual(str(user), "Hola")
        self.assertEqual(str(user2), "Some location")
