from django.urls import path

from . import views
from .views import export_csv, UserProfileSettingConfigView
from django.contrib.auth.decorators import login_required

# https://stackoverflow.com/questions/28555260/django-login-required-for-class-views


urlpatterns = [
    path("export/", views.export_csv, name="export_csv"),
    path(
        "",
        login_required(
            UserProfileSettingConfigView.as_view(
                template_name="user_profile_detail.html"
            )
        ),
        name="profile",
    ),
]
