from django.urls import path
from django_rest_passwordreset.views import reset_password_confirm
from django_rest_passwordreset.views import reset_password_request_token
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

from authentification import views

__all__ = []


app_name = "auth"

urlpatterns = [
    path(
        "",
        TokenObtainPairView.as_view(),
        name="authentification",
    ),
    path("refresh-token/", TokenRefreshView.as_view(), name="refresh-token"),
    path(
        "check-existance/",
        views.CheckExistanceView.as_view(),
        name="check-existance",
    ),
    path(
        "register/",
        views.RegistrationView.as_view(),
        name="register",
    ),
    path(
        "reset_password/", reset_password_request_token, name="reset_password"
    ),
    path(
        "reset_password/confirm/",
        reset_password_confirm,
        name="reset_password_confirm",
    ),
]
