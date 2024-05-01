from django.conf import settings
from django.http import JsonResponse
from rest_framework.views import APIView


__all__ = []


class GetNameView(APIView):
    """View for getting name of a site"""

    def get(self, request):
        """Get method"""
        return JsonResponse({"site_name": settings.SITE_NAME})
