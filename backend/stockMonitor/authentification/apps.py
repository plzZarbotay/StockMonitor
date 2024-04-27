from django.apps import AppConfig

__all__ = []


class AuthentificationConfig(AppConfig):
    """Authentification app config"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "authentification"

    def ready(self):
        """Function to register signals"""
        import authentification.signals

        authentification.signals
