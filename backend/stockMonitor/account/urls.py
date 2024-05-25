from django.urls import path

from account.views import GetUserProfile
from account.views import SetUserNameView
from account.views import ToggleUserThemeView

__all__ = []

app_name = "account"

urlpatterns = [
    path("get_profile/", GetUserProfile.as_view(), name="get_profile"),
    path("set_name/", SetUserNameView.as_view(), name="set_username"),
    path("switch_theme/", ToggleUserThemeView.as_view(), name="toggle_theme"),
    # добавить add_notification
]
