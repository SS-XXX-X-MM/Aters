from django.shortcuts import render
from django.views.generic import View
from Users.models import UserProfile
from Restaurants.models import RestaurantProfile

from Users.models import UserProfile

class DashboardHomeView(View):
    template = 'dashboard/dashboard_home.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            User = UserProfile.objects.get(user=request.user)
            city = User.address.city        # !Make sure Profile is complete, before allowing access to order
            restaurants = RestaurantProfile.objects.filter(address__city=city)
            context = {
                'restaurants': restaurants
            }
        else:
            context = {}
        return render(request, self.template, context)

    def post(self, request, *args, **kwargs):
        pass

