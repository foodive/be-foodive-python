from django.test import TestCase
from foodive import *
import foodive.models
from django.test import Client
from foodive.models import User
from django.db import models
# from .serializers import RestaurantSerializer
import foodive.views
import foodive.serializers
# import requests

from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.http import JsonResponse
import requests
import json
import random
from foodive.settings import YELP_API_KEY
from django.test.client import RequestFactory

class TestAppModels(TestCase):
    #
    # name = models.CharField(max_length=200)
    # location = models.CharField(max_length=200)
    def test_model_str(self):
        user = User.objects.create(name="Hola")
        user2 = User.objects.create(location="Some location")
        # assert user.name == "Hola"
        # assert user2.location == "Some location"
        # assert isinstance(name, str)
        self.assertEqual(str(user), "Hola")
        self.assertEqual(str(user2), "Some location")
