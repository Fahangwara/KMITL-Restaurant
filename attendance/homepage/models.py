from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Faculty(models.Model):
    name = models.CharField(max_length=100)

    
class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)
    picture = models.CharField(max_length=255)
    open_time = models.TimeField()
    close_time = models.TimeField()
    rating = models.IntegerField(blank=True)
    approve_by = models.CharField(max_length=50)
    approve_date = models.DateField()
    faculty_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)

class Food(models.Model):
    name = models.CharField(max_length=50)
    is_vegan = models.BooleanField()

class RestaurantFood(models.Model):
    price = models.FloatField()
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    food_id = models.ForeignKey(Food, on_delete=models.CASCADE)

class User(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)