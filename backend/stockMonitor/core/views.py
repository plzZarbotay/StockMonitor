from django.conf import settings
from django.http import JsonResponse
from drf_spectacular.utils import extend_schema, inline_serializer
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import CharField
from rest_framework.views import APIView

__all__ = []


class GetNameView(APIView):
    """View for getting name of a site"""

    @extend_schema(
        responses={
            200: inline_serializer(
                name="site_name_serializer", fields={"site_name": CharField()}
            )
        }
    )
    def get(self, request):
        """Method for getting name of a site"""
        return JsonResponse({"site_name": settings.SITE_NAME})


class GetNameView(APIView):
    """View for getting user first name"""

    permission_classes = [IsAuthenticated]

    def get(self, request):
        """Method for getting user first name"""
        name = request.user.first_name
        return JsonResponse({"first_name": name})


class UpdateFirstNameSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100)


class SetNameView(APIView):
    """Method for set user first name"""

    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=UpdateFirstNameSerializer,
        description="Set the first name of the authenticated user.",
        responses={200: "Success"},
    )
    def post(self, request):
        """Method for setting user first name"""
        serializer = UpdateFirstNameSerializer(data=request.data)
        if serializer.is_valid():
            first_name = serializer.validated_data.get("first_name")
            user = request.user
            user.first_name = first_name
            user.save()
            return JsonResponse(
                {"success": "First name updated successfully."}
            )
        else:
            return JsonResponse(serializer.errors, status=400)
