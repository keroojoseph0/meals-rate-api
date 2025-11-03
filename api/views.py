from django.shortcuts import render
from .models import Meal, Rate
from .serializers import MealSerializer, RateSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

# Create your views here.

class MealViewsets(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    
    '''
     - Update or Create rate for spacific meal on meal model
    '''
    @action(detail=True, methods=['POST'])
    def rate_meal(self, request, pk = None):
        
        if 'stars' in request.data:
            
            meal = Meal.objects.get(pk = pk)
            username = request.data['username']
            stars = request.data['stars']
            user = User.objects.get(username = username)
            
            try:
                # update
               rate = Rate.objects.get(user = user.id, meal = meal.id)
               rate.stars = stars
               rate.save()
               serializer = RateSerializer(rate)
               
               json = {
                   'message': 'Meal Rate Updated',
                   'result': serializer.data
               }
               return Response(json, status=status.HTTP_200_OK)
           
            except:
                # create
                
                rate = Rate.objects.create(user = user.id, meal = meal, stars = stars)
                serializer = RateSerializer(rate)
                
                json = {
                   'message': 'Meal Rate Create',
                   'result': serializer.data
               }
                
                return Response(json, status=status.HTTP_201_CREATED)
                
            
        else:
            json = {
                'message': 'stars not provided'
            }
            return Response(json, status=status.HTTP_400_BAD_REQUEST)
        
        
    
class RateViewsets(viewsets.ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
