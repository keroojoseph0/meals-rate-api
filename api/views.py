from django.shortcuts import render
from .models import Meal, Rate
from .serializers import MealSerializer, RateSerializer
from rest_framework import viewsets

# Create your views here.

class MealViewsets(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    
class RateViewsets(viewsets.ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
