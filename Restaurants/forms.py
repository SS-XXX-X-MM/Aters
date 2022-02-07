from django import forms
from Accounts.models import CustomUser
from django.contrib.auth import get_user_model

from Restaurants.models import FoodItem, RestaurantProfile

User = get_user_model()
spec_choice = (
    ("indian", "Indian"),
    ("chinese", "Chinese"),
    ("deserts", "Deserts")
)

class RestaurantCreationForm(forms.Form):
   email = forms.EmailField()
   mobile = forms.CharField(max_length=13)
   password = forms.CharField(strip=True)
   confirm_password = forms.CharField(strip=True)

   def clean_email(self):
      email = self.cleaned_data['email']
      email_already_exist = User.objects.filter(email__iexact=email).first()
      if email_already_exist:
         raise forms.ValidationError('Email already exists!')
      return email
   

   def clean(self):

      cleaned_data = super().clean()
      password = cleaned_data.get('password')
      confirm_password = cleaned_data.get('confirm_password')

      if len(confirm_password) < 7:
         raise forms.ValidationError("Password can't be less than 7 characters!")

      if password != confirm_password:
         raise forms.ValidationError("Passwords don't match!")


class AddFoodForm(forms.ModelForm):
   class Meta:
      model = FoodItem
      fields = ['food_name', 'food_type', 'food_price']

class RestaurantProfileForm(forms.Form):
   name = forms.CharField(max_length=100)
   started_on = forms.DateField()
   logo = forms.ImageField()
   speciality = forms.ChoiceField(choices=spec_choice)
   street = forms.CharField()
   locality = forms.CharField()
   city = forms.CharField()
   state = forms.CharField()
   pincode = forms.CharField()
   rating = forms.DecimalField(max_digits=2, decimal_places=1)
   

