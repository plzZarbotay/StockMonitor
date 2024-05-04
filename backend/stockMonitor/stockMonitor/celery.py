import os

from celery import Celery

__all__ = []


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "stockMonitor.settings")


app = Celery("backend")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
