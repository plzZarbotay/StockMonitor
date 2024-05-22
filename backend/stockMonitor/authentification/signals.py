from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created

__all__ = []


@receiver(reset_password_token_created)
def password_reset_token_created(
    sender, instance, reset_password_token, *args, **kwargs
):
    """
    Handles password reset tokens
    When a token is created, an e-mail needs to be sent to the user
    :param sender: View Class that sent the signal
    :param instance: View Instance that sent the signal
    :param reset_password_token: Token Model Object
    :param args:
    :param kwargs:
    :return:
    """
    context = {
        "current_user": reset_password_token.user,
        "email": reset_password_token.user.email,
        "reset_password_url": "{}?token={}".format(
            instance.request.build_absolute_uri(
                reverse("auth:reset_password_confirm")
            ),
            reset_password_token.key,
        ),
    }

    email_html_message = render_to_string(
        "authentification/forget_password.html", context
    )
    email_plaintext_message = render_to_string(
        "authentification/forget_password.txt", context
    )
    msg = EmailMultiAlternatives(
        "Сброс пароля для {title}".format(title=settings.SITE_NAME),
        email_plaintext_message,
        settings.EMAIL_ADDRESS,
        [reset_password_token.user.email],
    )
    msg.attach_alternative(email_html_message, "text/html")
    msg.send()
