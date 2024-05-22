from django.urls import path
from django_rest_passwordreset.views import reset_password_confirm
from django_rest_passwordreset.views import reset_password_request_token
from drf_spectacular.utils import extend_schema
from drf_spectacular.utils import extend_schema_view
from drf_spectacular.utils import inline_serializer
from drf_spectacular.utils import OpenApiResponse
from rest_framework.serializers import CharField
from rest_framework.serializers import ListField
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
    path("refresh_token/", TokenRefreshView.as_view(), name="refresh-token"),
    path(
        "check_existance/",
        views.CheckExistanceView.as_view(),
        name="check-existance",
    ),
    path(
        "register/",
        views.RegistrationView.as_view(),
        name="register",
    ),
    path(
        "reset_password/",
        extend_schema_view(
            post=extend_schema(
                description="Endpoint for creating request"
                " for password change",
                responses={
                    200: OpenApiResponse(
                        inline_serializer(
                            name="register_response_ok",
                            fields={"status": CharField()},
                        ),
                        description="Email found. Email sent",
                    ),
                    400: OpenApiResponse(
                        inline_serializer(
                            name="register_response_error",
                            fields={"email": ListField()},
                        ),
                        description="Error with email. Details in `email`",
                    ),
                },
            )
        )(reset_password_request_token),
        name="reset_password",
    ),
    path(
        "reset_password/confirm/",
        extend_schema_view(
            post=extend_schema(
                description="Endpoint for confirming password change."
                " Field `password` is a new password",
                responses={
                    200: OpenApiResponse(
                        inline_serializer(
                            name="change_password_ok",
                            fields={"status": CharField()},
                        ),
                        description="Password changed",
                    ),
                    404: OpenApiResponse(
                        inline_serializer(
                            name="change_password_error_404",
                            fields={"detail": CharField()},
                        ),
                        description="Password not changed,"
                        " maybe token expired",
                    ),
                    400: OpenApiResponse(
                        inline_serializer(
                            name="change_password_error_400",
                            fields={"password": ListField()},
                        ),
                        description="Password not changed,"
                        " password maybe small or something like that",
                    ),
                },
            )
        )(reset_password_confirm),
        name="reset_password_confirm",
    ),
]
