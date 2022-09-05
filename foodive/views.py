from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.http import JsonResponse

import requests
import json
import random

from .serializers import RestaurantSerializer
from .settings import YELP_API_KEY

class Restaurant:
  def restaurant_data(request):
      payload = {'location': request.GET.get('location',''),'categories': request.GET.get('categories','')}

      response = requests.get('https://api.yelp.com/v3/businesses/search', params=payload, headers={'Authorization': f'Bearer {YELP_API_KEY}'})

      restaurants = response.json()
      businesses = restaurants['businesses']
      rand_num = random.randint(0,len(businesses) - 1)
      return businesses[rand_num]

  def restaurant_response(request):
      serializer = RestaurantSerializer.serialize_data(Restaurant.restaurant_data(request))
      return JsonResponse({"data": serializer}, safe=False)
      pass
