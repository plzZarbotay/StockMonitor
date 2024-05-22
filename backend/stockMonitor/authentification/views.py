from django.http import JsonResponse
from drf_spectacular.utils import extend_schema
from drf_spectacular.utils import inline_serializer
from drf_spectacular.utils import OpenApiResponse
from rest_framework import status
from rest_framework.serializers import CharField
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from authentification import serializers
from core import models

__all__ = []


class RegistrationView(APIView):
    """View for registration"""

    authentication_classes = []
    serializer_class = serializers.RegisterSerializer

    @extend_schema(
        responses={
            201: inline_serializer(
                name="register_success",
                fields={"refresh": CharField(), "access": CharField()},
            )
        }
    )
    def post(self, request):
        """Endpoint for registration"""
        serializer = serializers.RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        refresh.payload.update(
            {
                "user_id": user.id,
                "username": user.email,
            }
        )
        return JsonResponse(
            {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            },
            status=status.HTTP_201_CREATED,
        )


class CheckExistanceView(APIView):
    """View for check if user exists"""

    authentication_classes = []
    serializer_class = serializers.CheckEmailExistanceSerializer

    @extend_schema(
        responses={
            204: OpenApiResponse(description="Email exists"),
            404: OpenApiResponse(description="Email doesnt exist"),
            400: OpenApiResponse(
                description="Wrong request, maybe email is incorrect"
            ),
        },
    )
    def post(self, request):
        """Endpoint for checking if user exists by email"""
        serializer = serializers.CheckEmailExistanceSerializer(
            data=request.data,
        )
        if serializer.is_valid(raise_exception=False):
            email = serializer.validated_data.pop("email")
            if models.User.objects.filter(email=email):
                return JsonResponse(data={}, status=status.HTTP_204_NO_CONTENT)
            return JsonResponse(data={}, status=status.HTTP_404_NOT_FOUND)
        return JsonResponse(data={}, status=status.HTTP_400_BAD_REQUEST)
