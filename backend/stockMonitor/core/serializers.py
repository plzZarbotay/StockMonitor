from rest_framework import serializers

__all__ = []


class PasswordField(serializers.CharField):
    """Custom Field for password"""
    def __init__(self, **kwargs):
        kwargs.setdefault("max_length", 32)
        kwargs.setdefault("min_length", 5)
        super().__init__(**kwargs)
