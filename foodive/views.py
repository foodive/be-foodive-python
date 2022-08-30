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
      "type": "object",
      "required": [
        "name",
        "image_url",
        "categories",
        "rating",
        "coordinates",
        "price",
        "location",
        "display_phone"
      ],
      "properties": {
        "name": {
          "type": "string",
          "examples": [
            rand_rest['name']
          ]
          },
        "image_url": {
          "type": "string",
          "examples": [
            rand_rest['image_url']
          ]
        },
        "categories": {
          "type": "array",
          "items": {
            "type": "object",
            "required": [
              "alias",
              "title"
            ],
            "properties": {
              "alias": {
                "type": "string",
                "examples": [
                  rand_rest['categories'][0]['alias']
                ]
              },
              "title": {
                "type": "string",
                "examples": [
                  rand_rest['categories'][0]['title']
                ]
              }
            },
            "examples": [{
              "alias": "newamerican",
              "title": "American (New)"
            },
             { "alias": "bakeries",
               "title": "Bakeries"
             },
              {
                "alias": "coffee",
                "title": "Coffee & Tea"
            }]
        }
      },
        "rating": {
          "type": "float",
          "default": 0.0,
          "examples": [
            rand_rest['rating']
          ]
        },
        "coordinates": {
          "type": "float",
          "required": [
            "latitude",
            "longitude"
          ],
          "properties": {
            "latitude": {
              "type": "float",
              "examples": [
                rand_rest['coordinates']['latitude']
              ]
            },
            "longitude": {
              "type": "float",
              "examples": [
                rand_rest['coordinates']['longitude']
              ]
            }
          },
          "examples": [{
            "latitude": rand_rest['coordinates']['latitude'],
            "longitude": rand_rest['coordinates']['longitude']
          }]
        },
        "price": {
          "type": "string",
          "examples": [
            rand_rest['price']
          ]
        },
        "location": {
          "type": "object",
          "required": [
            "displayed_address"
          ],
          "properties": {
            "display_address":{
              "type": "array",
              "items": {
                "type": "string",
                "examples": [
                  rand_rest['location']['display_address']
                ]
              }
            }
          }
        },
        "display_phone": {
          "type": "string",
          "examples": [
            rand_rest['display_phone']
            ]
          }
      }
    }

    # import ipdb; ipdb.set_trace()
    return JsonResponse({"restaurants": sample_dict}, safe=False)
    pass
