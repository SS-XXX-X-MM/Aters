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
    food_price = models.IntegerField()

    def __str__(self):
        return self.food_name


class Menu(models.Model):
    menu_item = models.ManyToManyField(FoodItem, related_name='menu')
    # menu_item_price = models.IntegerField() # -- menu specific price +

    def __str__(self):
        return "menu"
    

class RestaurantProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='restaurant_profile')
    name = models.CharField(max_length=100)
    started_on = models.DateField()
    logo = models.ImageField(default="restaurant_logo/default-restaurant-logo.jpg", upload_to="restaurant_logo/")
    speciality = models.CharField(max_length=100, choices=spec_choice, null=True, blank=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    menu = models.OneToOneField(Menu, on_delete=models.DO_NOTHING, related_name='restaurant')

    def __str__(self):
        return self.name

    

