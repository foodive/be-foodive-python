from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.http import JsonResponse
from .config import yelp_api_key
import requests
import json
import random
# from .serializers import RestaurantSerializer


def restaurant_data(request):
    payload = {'location': request.GET.get('location','')}
    response = requests.get('https://api.yelp.com/v3/businesses/search', params=payload, headers={'Authorization': yelp_api_key})

    restaurant = response.json()
    rand_num = random.randint(0,19)
    rand_rest = restaurant['businesses'][rand_num]
    sample_dict = {
        "id": "null",
        "type": "restaurant_info",
        "attributes": {
          "name": rand_rest['name'],
          "image_url": rand_rest['image_url'],
          "categories": {
            "category1": rand_rest['categories'][0]['title'],
            # "category2": rand_rest['categories'][1]['title'],
          },
          "rating": rand_rest['rating'],
          "coordinates": {
            "latitude": rand_rest['coordinates']['latitude'],
            "longitude": rand_rest['coordinates']['longitude']
          },
          "price": rand_rest['price'],
          "display_address": rand_rest['location']['display_address'],
          "display_phone": rand_rest['display_phone'],
    }
  }
 
    return JsonResponse({"data": sample_dict}, safe=False)
    pass
