from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

"""
| The following source has been used:
| https://stackoverflow.com/questions/28555260/django-login-required-for-class-views
| login_required: Enforces that the user is logged in.
"""
urlpatterns = [
    path("", login_required(views.dashboard_pie_chart), name="dashboard_pie_chart"),
]
