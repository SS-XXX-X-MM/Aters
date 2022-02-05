from random import choices
from django.db import models
from django.contrib.auth import get_user_model
from Accounts.models import Address
from Restaurants.models import RestaurantProfile, FoodItem
User = get_user_model()
gen_choices = (
    ("M", "Male"),
    ("F", "Female"),
    ("X", "Others")
)
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=100, choices=gen_choices)
    dob = models.DateField()
    profile_picture = models.ImageField(default="user_profile_pictures/default-profile-picture.jpg", upload_to="user_profile_pictures/")
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

class OrderCart(models.Model):
    customer = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    restaurant = models.OneToOneField(RestaurantProfile, on_delete=models.CASCADE)
    menu_food_item = models.OneToOneField(FoodItem, on_delete=models.CASCADE)
    menu_food_price = models.IntegerField()
    temp_address = models.TextField(null=True, blank=True)


