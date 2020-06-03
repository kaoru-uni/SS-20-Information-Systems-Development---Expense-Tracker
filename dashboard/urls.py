from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

# https://stackoverflow.com/questions/28555260/django-login-required-for-class-views


urlpatterns = [
    path("", login_required(views.dashboard_pie_chart), name="dashboard_pie_chart"),
]
