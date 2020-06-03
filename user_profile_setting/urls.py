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
    path("export-budget-csv/", views.export_budget_csv, name="export_budget_csv"),
    path("export-payment-csv/", views.export_payment_csv, name="export_payment_csv"),
]
