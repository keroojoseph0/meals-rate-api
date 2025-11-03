from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify
import uuid

# Create your models here.

class Meal(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    
    def no_of_rates(self):
        rates = Rate.objects.filter(meal = self)
        return rates.count()
    
    def avg_rates(self):
        rates = Rate.objects.filter(meal = self)
        sum = 0
        
        for i in rates:
            sum += i.stars
            
        if len(rates) > 0:
            return sum / int(rates.count())
        else:
            return 0

        
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
class Rate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    
    def __str__(self):
        return str(self.meal)
    
    class Meta:
        unique_together = (('user', 'meal'),)
        indexes = [
            models.Index(fields=['user', 'meal'], name='idx_rate_user_meal')
        ]
