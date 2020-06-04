from django.contrib import admin
from django.contrib.auth import views as auth_view
from django.urls import path, include

from register import views as register_view
from . import views

urlpatterns = [
    path("", views.welcome, name="welcome"),
    path("dashboard/", include("dashboard.urls")),
    path("category/", include("category.urls")),
    path("budget/", include("budget.urls")),
    path("admin/", admin.site.urls),
    path("register/", register_view.register, name="register"),
    path(
        "login/",
        auth_view.LoginView.as_view(template_name="register/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_view.LogoutView.as_view(template_name="register/logout.html"),
        name="logout",
    ),
    path("", include("django.contrib.auth.urls")),
    path("transaction/", include("transaction_expense.urls")),
    path("payment/", include("payment.urls")),
    path("profile/", include("user_profile_setting.urls")),
]
