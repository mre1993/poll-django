from django.urls import path, include
from .views import UserRegistrationView, LogoutView, LoginView

app_name = "accounts"

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("register/", UserRegistrationView.as_view(), name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
]