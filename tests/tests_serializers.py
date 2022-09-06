from django.test import TestCase
import foodive.views
from foodive.settings import YELP_API_KEY
from django.test.client import RequestFactory

def test_serializer():
    rf = RequestFactory()
    get_request = rf.get('/restaurants/?location=denver&categories=mexican')
    #instantiate request

    data = foodive.views.Restaurant.restaurant_data(get_request)
    #get data from the view

    serialized_data = foodive.serializers.RestaurantSerializer.serialize_data(data)
    #have the data serialized by the RestaurantSerializer

    assert isinstance(serialized_data['id'], str)
    assert isinstance(serialized_data['type'], str)
    assert isinstance(serialized_data['attributes'], dict)
    assert isinstance(serialized_data['attributes']['name'], str)
    assert isinstance(serialized_data['attributes']['image_url'], str)
    assert isinstance(serialized_data['attributes']['categories'], list)
    assert isinstance(serialized_data['attributes']['rating'], float)
    assert isinstance(serialized_data['attributes']['coordinates'], dict)
    assert isinstance(serialized_data['attributes']['coordinates']['latitude'], float)
    assert isinstance(serialized_data['attributes']['coordinates']['longitude'], float)
    assert isinstance(serialized_data['attributes']['price'], str)
    assert isinstance(serialized_data['attributes']['display_address'], list)
    assert isinstance(serialized_data['attributes']['display_phone'], str)

    #asserting that the return values are the appropriate data type (string, dictionary, float, list, etc.)
