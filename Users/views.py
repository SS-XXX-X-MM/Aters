from django.shortcuts import render
from django.views.generic import View
from .forms import UserCreationForm

class UserSignUpView(View):
    template = 'users/user_signup.html'
    form_class = UserCreationForm

    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, self.template, context)

    def post(self, request, *args, **kwargs):
        pass


class UserLoginView(View):
    template = 'users/user_login.html'
    # form_class = UserLoginForm

    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, self.template, context)

    def post(self, request, *args, **kwargs):
        pass
