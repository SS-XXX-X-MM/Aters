from django.shortcuts import redirect, render
from django.views.generic import View

from Users.models import OrderCart
from .forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib import messages
# from django_email_verification import send_email
from django.contrib.auth import authenticate, login, logout as django_logout
from django.contrib.auth.hashers import make_password
from Restaurants.models import FoodItem, RestaurantProfile

User = get_user_model()

class UserSignUpView(View):
    template = 'users/user_signup.html'
    form_class = UserCreationForm

    def get(self, request, *args, **kwargs):
        return render(request, self.template)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                email = form.cleaned_data['email'],
                password = form.cleaned_data['password'],
                mobile = form.cleaned_data['mobile'],
                is_active = True  # Do this by sending mail
            )

            user.save()
            # send_email(user)
            messages.info(request, 'Account created successfully, email has been sent to activate your account!')
            return redirect('user_login')
        else:
            messages.error(request, 'Please fill details correctly!')
        return render(request, self.template, {'form':form})



class UserLoginView(View):
    template = 'users/user_login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template)

    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.get(email=email)
        except Exception as e:
            messages.error(request, "User doesn't exist with the entered credentials, please enter correct credentials!")
            return redirect('user_login')
        # password = make_password(password)
        user = authenticate(request, email=email, password=password)
        if user is not None and user.is_user:
            login(request, user)
            messages.info(request, 'Logged In')
            return redirect('dashboard_home')
        else:
            messages.error(request, 'Incorrect Username or Password!')
            return redirect('user_login')


def logout(request):
    '''function to handle logout request'''
    messages.success(request,'Logged out successfully!')
    django_logout(request)
    return redirect('dashboard_home')


class UserProfileView(View):
    
    def get(self, request, *args, **kwargs):
        pass


class UserOrderView(View):
    template = 'users/user_order.html'
    def get(self, request, id, *args, **kwargs):
        restaurant = RestaurantProfile.objects.get(id=id)
        menu = restaurant.menu.menu_item.all()
        context = {
            'id':id,
            'menu':menu
        }
        return render(request, self.template, context)

    def post(self, request, *args, **kwargs):
        print()
        restaurant = RestaurantProfile.objects.get(id=request.POST['restaurant_id']) 
        food_item = FoodItem.objects.get(id=request.POST['food_id']) 
        food_price = request.POST['food_price']
        customer = request.user.userprofile
        # quantity = request.POST['qty']
        print(food_item)
        print(request.POST['food_id'])

        order = OrderCart(customer=customer, restaurant=restaurant, menu_food_item=food_item, menu_food_price=food_price)
        order.save()
        messages.success(request, "Added to Cart!")
        print(request.path)
        return redirect('dashboard_home')

        
