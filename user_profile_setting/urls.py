from django.urls import path

from . import views
from .views import export_csv, UserProfileSettingConfigView

urlpatterns = [
    path("export/", views.export_csv(), name="profile"),
    path("profile/", UserProfileSettingConfigView.as_view(), name="profile"),
]
