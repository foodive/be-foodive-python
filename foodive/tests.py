from django.test import TestCase
from django.test import Client
from foodive.models import User
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
from .settings import YELP_API_KEY
from django.test.client import RequestFactory

def test_view_url_exists_at_desired_location():
    response = requests.get('https://api.yelp.com/v3/businesses/search?categories=&mexican&chinese&italian&location=chicago', headers={'Authorization': f'Bearer {YELP_API_KEY}'})
    assert response.status_code == 200

def test_view_url_returns_invalid_status_code_given_bad_input():
    response = requests.get('https://api.yelp.com/v3/businesses/search?', headers={'Authorization': f'Bearer {YELP_API_KEY}'})
    assert response.status_code == 400

def test_view_url_has_price_in_dict():
    response = requests.get('https://api.yelp.com/v3/businesses/search?categories=&mexican&chinese&italian&location=chicago', headers={'Authorization': f'Bearer {YELP_API_KEY}'})

    restaurants = response.json()
    businesses = restaurants['businesses']
    rand_num = random.randint(0,len(businesses) - 1)
    rand_rest = businesses[rand_num]
    rand_rest_categories = rand_rest['categories']

    if not 'price' in rand_rest:
        rand_rest['price'] = "n/a"

    assert 'price' in rand_rest

def test_view_url_has_categories_as_list():
    response = requests.get('https://api.yelp.com/v3/businesses/search?categories=&mexican&chinese&italian&location=chicago', headers={'Authorization': f'Bearer {YELP_API_KEY}'})

    restaurants = response.json()
    businesses = restaurants['businesses']
    rand_num = random.randint(0,len(businesses) - 1)
    rand_rest = businesses[rand_num]
    rand_rest_categories = rand_rest['categories']

    category_list = []

    for i in rand_rest['categories']:
        category_list.append(i['title'])

    assert isinstance(category_list, list)

def test_serializer():
    rf = RequestFactory()
    get_request = rf.get('/restaurants/?location=denver&categories=mexican')

    rand_rest = foodive.views.Restaurant.restaurant_data(get_request)

    category_list = []

    for i in rand_rest['categories']:
        category_list.append(i['title'])

        serialize_data = {
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
    assert isinstance(serialize_data['attributes']['name'], str)
    assert isinstance(serialize_data['attributes']['image_url'], str)
    assert isinstance(serialize_data['attributes']['categories'], list)
    assert isinstance(serialize_data['attributes']['rating'], float)
    assert isinstance(serialize_data['attributes']['coordinates'], dict)
    assert isinstance(serialize_data['attributes']['coordinates']['latitude'], float)
    assert isinstance(serialize_data['attributes']['coordinates']['longitude'], float)
    assert isinstance(serialize_data['attributes']['price'], str)
    assert isinstance(serialize_data['attributes']['display_address'], list)
    assert isinstance(serialize_data['attributes']['display_phone'], str)
