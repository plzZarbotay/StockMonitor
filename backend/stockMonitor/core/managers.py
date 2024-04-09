from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import UserManager as BaseUserManager

__all__ = []


class UserManager(BaseUserManager):
    """Override BaseUserManager to add custom user model"""
    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        print(email)
        user = self.model(email=email, **extra_fields)
        print(1)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        """Method to create user"""
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        print()
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        """Method to create superuser"""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)
