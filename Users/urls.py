from django.urls import path
from .views import UserSignUpView, UserLoginView, logout
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', UserLoginView.as_view(), name='user_login'),
    path('signup/', UserSignUpView.as_view(), name = 'user_signup'),
    path('logout/', login_required(logout), name='user_logout'),
]