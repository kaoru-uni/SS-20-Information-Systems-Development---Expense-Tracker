from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard_pie_chart, name="dashboard_pie_chart"),
]
