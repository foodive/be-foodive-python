from rest_framework import serializers
import rest_framework.views 

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        x = rest_framework.views.restaurant_data()
        fields = x['businesses'][0]['name']
        import ipdb; ipdb.set_trace()


