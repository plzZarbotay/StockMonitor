from django.contrib import admin
from django.contrib.admin import AdminSite as BaseAdminSite
from django.template.response import TemplateResponse
from django.urls import path

from core.tasks import delete_all_stock_data_task
from core.tasks import get_candles_task
from core.tasks import get_companies
from stocks.models import Stock

__all__ = []


class AdminSite(BaseAdminSite):
    """Override of basic admin site"""

    def get_urls(self):
        """Override of basic get urls"""
        url = [
            path(
                "special/",
                self.admin_view(self.special_commands),
                name="special_admin",
            )
        ]
        urls = super(AdminSite, self).get_urls()

        return url + urls

    def special_commands(self, request):
        """View function for special commands"""
        if request.method == "POST":
            parse_data = request.POST.get("parse")
            if parse_data == "companies":
                get_companies.delay()
            elif parse_data == "candles":
                get_candles_task.delay(ticker="YNDX")
            elif parse_data == "candlesAll":
                for company in Stock.objects.all():
                    get_candles_task.delay(ticker=company.ticker)
            elif parse_data == "data_clean":
                delete_all_stock_data_task.delay()

        context = dict(
            **self.each_context(request),
        )
        request.current_app = self.name
        return TemplateResponse(request, "admin/special.html", context)


admin.site = AdminSite()
