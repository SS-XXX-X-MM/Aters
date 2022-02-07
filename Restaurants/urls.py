from django.urls import path
from .views import RestaurantHomeView, RestaurantLoginView, RestaurantSignupView, logout, RestaurantOrdersView, RestaurantMenuView, RestaurantAddFood,RestaurantProfileView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', RestaurantHomeView.as_view(), name='restaurant_home'),
    path('login/', RestaurantLoginView.as_view(), name = 'restaurant_login'),
    path('signup/', RestaurantSignupView.as_view(), name = 'restaurant_signup'),
    path('logout/', login_required(logout), name='restaurant_logout'),
    path('profile/', RestaurantProfileView.as_view(),name='restaurant_profile'),
    path('orders/', RestaurantOrdersView.as_view(), name='restaurant_orders'),
    path('menu/', RestaurantMenuView.as_view(), name='restaurant_menu'),
    path('add_food/', RestaurantAddFood.as_view(), name='restaurant_add_food')
    
]