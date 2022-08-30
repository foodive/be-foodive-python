from django.test import TestCase
from django.test import unittest
from django.test import Client

c = Client()
response = c.get('https://api.yelp.com/v3/businesses/search', params=payload, headers={'Authorization': YELP_API_KEY})
response.content
