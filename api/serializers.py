from rest_framework import serializers
from .models import Meal, Rate


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ['slug', 'title', 'description']
        
        
class RateSerializer(serializers.ModelSerializer):
    meal = serializers.StringRelatedField()
    user = serializers.CharField(source = 'user.username', read_only = True)
    
    class Meta:
        model = Rate
        fields = ['id', 'meal', 'user', 'stars']
