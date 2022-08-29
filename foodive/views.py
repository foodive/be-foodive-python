from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import requests
# from .serializers import RestaurantSerializer


def restaurant_data(request):
    response = requests.get('https://api.yelp.com/v3/businesses/search?location=chicago', headers={'Authorization': 'Bearer llFKl4YQSGryN4AvEdCkWS13yYb-sNbueMcFrEvwGBdBu8Sk8RIG3kSeod9p5ksV2CJfk969a8AoCA4EovVLl3FgCDZ6ZQeHZ0jGslV4VyHHxkKKiYt7ENagrCjxYnYx'})


    restaurant = response.json()
    # serializer = RestaurantSerializer(response, many=True)
    # return JsonResponse({"data": response.json()}, safe=False)
    return JsonResponse({"restaurants": restaurant}, safe=False)
    pass
