from rest_framework import serializers
import foodive.views

class RestaurantSerializer:
    def serialize_data(rand_rest):
        rand_rest_categories = rand_rest['categories']

        category_list = []

        for i in rand_rest['categories']:
          category_list.append(i['title'])

        if not 'price' in rand_rest:
          rand_rest['price'] = "n/a"
        
        return {
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