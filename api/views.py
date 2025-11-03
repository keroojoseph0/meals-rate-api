from django.shortcuts import render
from .models import Meal, Rate
from .serializers import MealSerializer, RateSerializer, UserSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly

# Create your views here.

class Userviewsets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    authentication_classes = [TokenAuthentication,]
    permission_classes = [AllowAny,]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_except = True)
        self.perform_create(serializer)
        
        token, created = Token.objects.get_or_create(user = serializer.instance)
        
        return Response ({
            'token': token.key
        }, status=status.HTTP_201_CREATED)
        
        def list(self, request, *args, **kwargs):
            response = {
                'message': "you can't create rating like that"
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        
class MealViewsets(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    
    '''
     - Update or Create rate for spacific meal on meal model
    '''
    @action(detail=True, methods=['POST'])
    def rate_meal(self, request, pk = None):
        
        if 'stars' in request.data:
            
            meal = Meal.objects.get(pk = pk)
            stars = request.data['stars']
            user = request.user
            
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
    
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    
    def update(self, request, *args, **kwargs):
        json = {
            'message': 'Invalid way to create or update'
        }
        
        return  Response(json, status=status.HTTP_400_BAD_REQUEST)
    
    def create(self, request, *args, **kwargs):
        json = {
            'message': 'Invalid way to create or update'
        }
        
        return  Response(json, status=status.HTTP_400_BAD_REQUEST)
