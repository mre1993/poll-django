from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, LoginForm
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .models import User


class UserRegistrationView(View):
    form_class = UserRegistrationForm
    template_name = "accounts/register.html"

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User(
                phone_number=cd["phone_number"],
                email=cd["email"],
                about_me=cd["about_me"],
                first_name=cd["first_name"],
                last_name=cd["last_name"],
            )
            user.set_password(cd["password2"])
            user.save()
            login(request, user)
            return redirect("player:vote")
        return render(request, self.template_name, {"form": form})


class LoginView(View):
    form_class = LoginForm
    template_name = "accounts/login.html"

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data["phone_number"]
            password = form.cleaned_data["password"]
            user = authenticate(request, phone_number=phone_number, password=password)
            if user is not None:
                login(request, user)
                return redirect("player:vote")
        return render(request, self.template_name, {"form": form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return render(request, "accounts/logout.html")

