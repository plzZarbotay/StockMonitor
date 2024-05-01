from django.http import JsonResponse
from rest_framework.views import APIView

from stocks.models import Stock

__all__ = []


class MarketView(APIView):
    """Market view"""

    def get(self, request):
        """Get method with q parameter"""
        search_stock = request.GET.get("q", None)
        stocks = Stock.objects.search_for_stock(search_stock)
        json_data = list(stocks.values())
        return JsonResponse(json_data, safe=False)
