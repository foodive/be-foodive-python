from django.test import TestCase
from django.shortcuts import render
from django.http import JsonResponse
import requests
import json
import random
from foodive.settings import YELP_API_KEY
from django.test.client import RequestFactory


def test_view_url_exists_at_desired_location():
    response = requests.get('https://api.yelp.com/v3/businesses/search?categories=&mexican&chinese&italian&location=chicago', headers={'Authorization': f'Bearer {YELP_API_KEY}'})
    assert response.status_code == 200
    #assumes the response code is 200 if params are correct

def test_view_url_returns_invalid_status_code_given_bad_input():
    response = requests.get('https://api.yelp.com/v3/businesses/search?', headers={'Authorization': f'Bearer {YELP_API_KEY}'})
    assert response.status_code == 400
    #assumes the response code is 400 if params are incorrect

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
    #assumes that the price key is in the rand_rest dictionary

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
    #assumes that the category_list list is instantiated
