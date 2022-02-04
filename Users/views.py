from django.shortcuts import redirect, render
from django.views.generic import View
from .forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib import messages
# from django_email_verification import send_email
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password

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
                first_name = form.cleaned_data['first_name'],
                last_name = form.cleaned_data['last_name'],
                mobile = form.cleaned_data['mobile']
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
        if user is not None:
            login(request, user)
            messages.info(request, 'Logged In')
            return redirect('dashboard_home')
        else:
            messages.error(request, 'Incorrect Username or Password!')
            return redirect('user_login')
