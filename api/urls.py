from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('meals', views.MealViewsets)
router.register('rates', views.RateViewsets)


app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
]
