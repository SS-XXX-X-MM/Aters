from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect, render
from django.views.generic import View
from .forms import RestaurantCreationForm
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

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
                mobile = form.cleaned_data['mobile']
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
        if user is not None:
            login(request, user)
            messages.info(request, 'Logged In')
            return redirect('restaurant_home')
        else:
            messages.error(request, 'Incorrect Username or Password!')
            return redirect('restaurant_login')