"""expense_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_view
from django.urls import path, include
from payment.views import PaymentConfigView
from payment.views import amount_insert
from user import views as user_views
from register import views as register_view
from register import views as v
from category import views as category_views
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("category/", category_views.CategoryView.as_view()),
    path("admin/", admin.site.urls),
    path("register/", register_view.register, name="register"),
    path("profile/", user_views.profile, name="profile"),
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
    path("payment/", PaymentConfigView.as_view()),
    path("all_payment/", amount_insert),
    path("", include("django.contrib.auth.urls")),
]
