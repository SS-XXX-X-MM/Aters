from django.urls import path
from .views import UserSignUpView, UserLoginView, logout, UserProfileView, UserOrderView, UserCartView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', UserLoginView.as_view(), name='user_login'),
    path('signup/', UserSignUpView.as_view(), name = 'user_signup'),
    path('logout/', login_required(logout), name='user_logout'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    # path('explore/', UserExploreView.as_view(), name='user_explore'),
    path('order/<int:id>', UserOrderView.as_view(), name='user_order'),
    path('mycart/', UserCartView.as_view(), name='user_cart'),
]