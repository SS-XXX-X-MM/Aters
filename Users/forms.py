from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


User = get_user_model()
gen_choices = (
    ("M", "Male"),
    ("F", "Female"),
    ("X", "Others")
)

class UserCreationForm(forms.Form):
   # first_name = forms.CharField(strip=True)
   # last_name = forms.CharField(strip=True)
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


class UserProfileForm(forms.Form):
   first_name = forms.CharField(max_length=100)
   last_name = forms.CharField(max_length=100)
   gender = forms.ChoiceField(choices=gen_choices)
   dob = forms.DateField()
   profile_picture = forms.ImageField()
   street = forms.CharField(max_length=100)
   locality = forms.CharField()
   city = forms.CharField()
   state = forms.CharField()
   pincode = forms.CharField()

