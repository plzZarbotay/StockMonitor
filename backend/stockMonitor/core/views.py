from django.conf import settings
from django.http import JsonResponse
from drf_spectacular.utils import extend_schema
from drf_spectacular.utils import inline_serializer
from rest_framework.serializers import CharField
from rest_framework.views import APIView

__all__ = []


class GetNameView(APIView):
    """View for getting name of a site"""

    authentication_classes = []

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
