# from django.http import JsonResponse
# from .models import User
# from .serializers import UserSerializer
#
# def user_list(request):
#
#     #get all drinks, serailize them, return json
#
#     drinks = Drink.objects.all()
#
#     serailizer = DrinkSerializer(drinks, many=True)
#     return JsonResponse({"drinks": serailizer.data}, safe=False)

from django.shortcuts import render
from django.http import HttpResponse
import requests


def restaurant_data():
    category = 'mexican'
    location = 'chicago'

    # response = requests.get('[https://api.yelp.com/v3/businesses/search?categories=&{category}&location={location}],headers={'Authorization: Bearer <API KEY>'})')
    # requests.get("https://api.yelp.com/v3/autocomplete?text=del&latitude=37.786882&longitude=-122.399972",headers={'Authorization: Bearer <API KEY>'})
    response = requests.get('https://api.yelp.com/v3/businesses/search?location=chicago', headers={'Authorization': 'Bearer llFKl4YQSGryN4AvEdCkWS13yYb-sNbueMcFrEvwGBdBu8Sk8RIG3kSeod9p5ksV2CJfk969a8AoCA4EovVLl3FgCDZ6ZQeHZ0jGslV4VyHHxkKKiYt7ENagrCjxYnYx'})


    restaurant = response.json()

    return restaurant
    pass



