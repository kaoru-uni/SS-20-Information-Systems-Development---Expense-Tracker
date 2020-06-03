from django.urls import path

from . import views
from .views import export_csv, UserProfileSettingConfigView

urlpatterns = [
    path("export/", views.export_csv, name="export_csv"),
    path(
        "",
        UserProfileSettingConfigView.as_view(template_name="user_profile_detail.html"),
        name="profile",
    ),
]
