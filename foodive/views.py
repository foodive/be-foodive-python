from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.http import JsonResponse
# from .config import yelp_api_key
import requests
import json
import random
from .settings import YELP_API_KEY

def restaurant_data(request):
    # import ipdb; ipdb.set_trace()

    payload = {'location': request.GET.get('location',''),'categories': request.GET.get('categories','')}

    response = requests.get('https://api.yelp.com/v3/businesses/search', params=payload, headers={'Authorization': f'Bearer {YELP_API_KEY}'})

    restaurants = response.json()
    businesses = restaurants['businesses']
    rand_num = random.randint(0,len(businesses) - 1)
    rand_rest = businesses[rand_num]
    rand_rest_categories = rand_rest['categories']

    category_list = []

    for i in rand_rest['categories']:
        category_list.append(i['title'])

    if not 'price' in rand_rest:
        rand_rest['price'] = "n/a"


    sample_dict = {
        "id": "null",
        "type": "restaurant_info",
        "attributes": {
          "name": rand_rest['name'],
          "image_url": rand_rest['image_url'],
          "categories": category_list,
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
