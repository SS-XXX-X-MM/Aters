from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect, render
from django.views.generic import View
from .forms import RestaurantCreationForm, AddFoodForm, RestaurantProfileForm
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout as django_logout
from .models import *
from Users.models import OrderCart

User = get_user_model()

class RestaurantHomeView(View):
    template = 'restaurant/restaurant_home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template)


class RestaurantSignupView(View):
    template = 'restaurant/restaurant_signup.html'
    form_class = RestaurantCreationForm

    def get(self, request, *args, **kwargs):
        return render(request, self.template)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                email = form.cleaned_data['email'],
                password = form.cleaned_data['password'],
                mobile = form.cleaned_data['mobile'],
                is_active = True,  # Do this by sending mail
                is_restaurant = True,
                is_user = False
            )
            
            user.save()
            messages.info(request, 'Account created successfully!')
            return redirect('restaurant_login')
        else:
            messages.error(request, 'Please fill details correctly!')
        return render(request, self.template, {'form':form})



class RestaurantLoginView(View):
    template = 'restaurant/restaurant_login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template)

    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.get(email=email)
        except Exception as e:
            messages.error(request, "Restaurant doesn't exist with the entered credentials, please enter correct credentials!")
            return redirect('restaurant_login')
        # password = make_password(password)
        user = authenticate(request, email=email, password=password)
        if user is not None and user.is_restaurant:
            login(request, user)
            messages.info(request, 'Logged In')
            return redirect('restaurant_home')
        else:
            messages.error(request, 'Incorrect Username or Password!')
            return redirect('restaurant_login')


def logout(request):
    '''function to handle logout request'''
    messages.success(request,'Logged out successfully!')
    django_logout(request)
    return redirect('restaurant_home')


class RestaurantMenuView(View):
    template = 'restaurant/restaurant_menu.html'

    def get(self, request, *args, **kwargs):
        try:
            user = RestaurantProfile.objects.get(user=request.user)
            menu = user.menu.menu_item.all()
            context = {
                'menu':menu
            }
        except:
            context = {}              #no menu or update your profile
        return render(request, self.template, context)


class RestaurantOrdersView(View):
    template = 'restaurant/restaurant_orders.html'
    
    def get(self, request, *args, **kwargs):
        try:
            user = RestaurantProfile.objects.get(user=request.user)
            orders = OrderCart.objects.filter(restaurant=user)
            context = {
                'orders':orders
            }
        except:
            context={}              #no orders or update your profile
        return render(request, self.template, context)


class RestaurantAddFood(View):
    template = 'restaurant/restaurant_addfood.html'
    form_class = AddFoodForm

    def get(self, request, *args, **kwargs):
        return render(request, self.template)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            try:
                restaurant = request.user.restaurantprofile
                item = form.save()
                restaurant.menu.menu_item.add(item)
                messages.success(request, "Item added to the menu!")
            except:
                messages.error(request, "Update Your Profile!")
        else:
            messages.error(request, "Incorrect Entries!")

        return redirect('restaurant_menu')


class RestaurantProfileView(View):
    template = 'restaurant/restaurant_profile.html'
    form_class = RestaurantProfileForm

    def get(self, request, *args, **kwargs):
        try:
            User = request.user.restaurantprofile
            context = {'User':User}
        except:
            context = {}
        return render(request, self.template, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            street = form.cleaned_data.get('street')
            locality =  form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state =  form.cleaned_data['state']
            pincode =  form.cleaned_data['pincode']
            name = form.cleaned_data['name']
            started_on = form.cleaned_data['started_on']
            speciality = form.cleaned_data['speciality']
            rating = form.cleaned_data['rating']
            logo = form.cleaned_data['logo']

            try:
                restaurant = request.user.restaurantprofile
                addr = restaurant.address
                addr.street=street
                addr.locality=locality
                addr.city=city
                addr.state=state
                addr.pincode=pincode
                addr.save()
                restaurant.name=name
                restaurant.started_on=started_on
                restaurant.rating=rating
                restaurant.speciality=speciality
                restaurant.logo=logo
                restaurant.address=addr
                restaurant.save()
            except:
                menu = Menu()
                menu.save()
                addr = Address.objects.create(street=street, locality=locality, city=city, state=state, pincode=pincode)
                newrestaurant = RestaurantProfile.objects.create(user=request.user, name=name, started_on=started_on, speciality=speciality, rating=rating, logo=logo, address=addr, menu=menu)

            messages.success(request, "Profile Created Successfully!")
        else:
            messages.error(request, "Incorrect data")
        return redirect('restaurant_home')