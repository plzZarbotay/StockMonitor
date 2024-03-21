import os

from django.core.asgi import get_asgi_application

__all__ = []

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "stockMonitor.settings")

application = get_asgi_application()
