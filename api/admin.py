from django.contrib import admin
from .models import Meal, Rate

# Register your models here.

@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    list_filter = ['title']
    search_fields = ['title']


class RateAdmin(admin.ModelAdmin):
    list_display = ['meal', 'user', 'stars']
    list_filter = ['stars']
    
admin.site.register(Rate, RateAdmin)
