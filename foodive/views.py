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

def restaurant_data(request):
    category = 'mexican'
    location = 'chicago'
    # response = requests.get('[https://api.yelp.com/v3/businesses/search?categories=&{category}&location={location}],headers={'Authorization: Bearer <API KEY>'})')
    # requests.get("https://api.yelp.com/v3/autocomplete?text=del&latitude=37.786882&longitude=-122.399972",headers={'Authorization: Bearer <API KEY>'})
    requests.get("https://api.yelp.com/v3/businesses/search?categories=&{category}&location={location}",headers={'Authorization: Bearer <API KEY>'})

    restaurant = response.json()
    print(restaurant)
    return HttpResponse("restaurant")
    pass
