from rest_framework import serializers
from .models import Meal, Rate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {
            'password': {'write_only': True, 'required': True} # not return password in response
        }
        
class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ['slug', 'title', 'description', 'no_of_rates', 'avg_rates']
        
        
class RateSerializer(serializers.ModelSerializer):
    meal = serializers.StringRelatedField()
    user = serializers.CharField(source = 'user.username', read_only = True)
    
    class Meta:
        model = Rate
        fields = ['id', 'meal', 'user', 'stars']
