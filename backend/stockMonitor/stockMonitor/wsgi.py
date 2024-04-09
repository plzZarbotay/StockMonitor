import os

from django.core.wsgi import get_wsgi_application

__all__ = []

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "stockMonitor.settings")

application = get_wsgi_application()
