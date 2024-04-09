from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

from authentification import views

__all__ = []


app_name = "auth"

urlpatterns = [
    path(
        "authentificate/",
        TokenObtainPairView.as_view(),
        name="authentification",
    ),
    path("refresh-token/", TokenRefreshView.as_view(), name="refresh-token"),
    path(
        "authentificate/check-existance/",
        views.CheckExistanceView.as_view(),
        name="check-existance",
    ),
    path(
        "register/",
        views.RegistrationView.as_view(),
        name="register",
    ),
]
