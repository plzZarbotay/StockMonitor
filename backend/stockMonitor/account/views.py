from django.http import JsonResponse
from drf_spectacular.utils import extend_schema
from drf_spectacular.utils import inline_serializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import CharField
from rest_framework.views import APIView

import account.serializers
import core.models

__all__ = []


class GetUserProfile(APIView):
    """View for getting user profile data"""

    permission_classes = [IsAuthenticated]
    serializer_class = account.serializers.GetUserProfileSerializer

    def get(self, request):
        """Endpoint for getting user profile data"""
        return JsonResponse(
            account.serializers.GetUserProfileSerializer(request.user).data,
            status=status.HTTP_200_OK,
        )


class SetUserNameView(APIView):
    """Method for set user first name"""

    permission_classes = [IsAuthenticated]
    serializer_class = account.serializers.UpdateFirstNameSerializer

    @extend_schema(
        description="Set the first name of the authenticated user.",
        responses={
            200: inline_serializer(
                name="set_user_name_success",
                fields={"success": CharField()},
            ),
            400: inline_serializer(
                name="set_user_name_error",
                fields={"detail": CharField()},
            ),
        },
    )
    def post(self, request):
        """Method for setting user first name"""
        serializer = account.serializers.UpdateFirstNameSerializer(
            data=request.data
        )
        if serializer.is_valid():
            first_name = serializer.validated_data.get("first_name")
            user = request.user
            user.first_name = first_name
            user.save()
            return JsonResponse(
                {"success": "First name updated successfully."},
                status=status.HTTP_200_OK,
            )
        return JsonResponse(
            {"detail": "Error occurred"}, status=status.HTTP_400_BAD_REQUEST
        )


class ToggleUserThemeView(APIView):
    """Method for toggling user theme"""

    permission_classes = [IsAuthenticated]

    @extend_schema(
        responses={
            200: inline_serializer(
                name="toggle_response_success",
                fields={"success": CharField()},
            )
        }
    )
    def post(self, request):
        """Method for setting user first name"""
        user = request.user
        if user.theme == core.models.User.Themes.LIGHT:
            user.theme = core.models.User.Themes.DARK
        else:
            user.theme = core.models.User.Themes.LIGHT
        user.save()
        return JsonResponse({"success": f"Theme changed to {user.theme}"})
