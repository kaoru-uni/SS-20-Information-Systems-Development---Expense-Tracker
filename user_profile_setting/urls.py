from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views
from .views import UserProfileSettingConfigView

"""
| The following source has been used:
| https://stackoverflow.com/questions/28555260/django-login-required-for-class-views
| login_required: Enforces that the user is logged in.
"""
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
    path("export-budget-csv/", views.export_budget_csv, name="export_budget_csv"),
    path("export-payment-csv/", views.export_payment_csv, name="export_payment_csv"),
    path('transaction_upload/', views.transaction_upload, name="transaction_upload"),
]
