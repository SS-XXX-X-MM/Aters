from django.urls import path
from .views import RestaurantHomeView, RestaurantLoginView, RestaurantSignupView

urlpatterns = [
    path('', RestaurantHomeView.as_view(), name='restaurant_home'),
    path('login/', RestaurantLoginView.as_view(), name = 'restaurant_login'),
    path('signup/', RestaurantSignupView.as_view(), name = 'restaurant_signup'),
]