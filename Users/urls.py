from django.urls import path
from .views import UserSignUpView, UserLoginView

urlpatterns = [
    path('', UserLoginView.as_view(), name='user_login'),
    path('signup/', UserSignUpView.as_view(), name = 'user_signup'),
]