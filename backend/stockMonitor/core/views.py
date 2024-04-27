from django.http import JsonResponse

from rest_framework.views import APIView
from django.conf import settings


class GetNameView(APIView):
    def get(self, request):
        return JsonResponse({"site_name": settings.SITE_NAME})
