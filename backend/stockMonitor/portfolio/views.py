from django.db import transaction
from rest_framework.views import APIView
from portfolio.models import Portfolio
from django.http import JsonResponse
import portfolio.serializers

__all__ = []


class TransactionsView(APIView):
    serializer_class = portfolio.serializers.TransactionsSerializer

    def post(self, request):
        serializer = portfolio.serializers.TransactionsSerializer(
            data=request.data
        )
        serializer.is_valid()
        data = serializer.validated_data
        serializer.save()


class PortfolioTableView(APIView):
    serializer_class = portfolio.serializers.PortfolioSerializer

    def get(self, request):
        portfolios = Portfolio.objects.all()
        serializer = self.serializer_class(portfolios, many=True)
        return JsonResponse(serializer.data, safe=False)
