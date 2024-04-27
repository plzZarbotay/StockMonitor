from django.http import JsonResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from authentification import serializers
from core import models

__all__ = []


class RegistrationView(APIView):
    """View for registration"""

    serializer_class = serializers.RegisterSerializer

    def post(self, request):
        """Post method"""
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

    serializer_class = serializers.CheckEmailExistanceSerializer

    def post(self, request):
        """Post method"""
        serializer = serializers.CheckEmailExistanceSerializer(
            data=request.data,
        )
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.pop("email")
        if models.User.objects.filter(email=email):
            return JsonResponse(data={}, status=status.HTTP_204_NO_CONTENT)
        return JsonResponse(data={}, status=status.HTTP_404_NOT_FOUND)


class ChangePasswordView(APIView):
    """View for change password"""
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """Post method"""
        serializer = serializers.ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            if user.check_password(serializer.data.get("old_password")):
                user.set_password(serializer.data.get("new_password"))
                user.save()
                return JsonResponse(
                    {"message": "Password changed successfully."},
                    status=status.HTTP_200_OK,
                )
            return JsonResponse(
                {"error": "Incorrect old password."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return JsonResponse(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )
