from django.db import models
from django.contrib.auth import get_user_model
from Accounts.models import Address

User = get_user_model()
spec_choice = (
    ("indian", "Indian"),
    ("chinese", "Chinese"),
    ("deserts", "Deserts")
)

class FoodItem(models.Model):
    food_name = models.CharField(max_length=100)
    food_type = models.CharField(max_length=100)


class Menu(models.Model):
    menu_item = models.ManyToManyField(FoodItem)
    menu_item_price = models.IntegerField()
    

class RestaurantProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    started_on = models.DateField()
    logo = models.ImageField(default="restaurant_logo/default-restaurant-logo.jpg", upload_to="restaurant_logo/")
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    speciality = models.CharField(max_length=100, choices=spec_choice, null=True, blank=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    menu = models.OneToOneField(Menu, on_delete=models.CASCADE)


    

