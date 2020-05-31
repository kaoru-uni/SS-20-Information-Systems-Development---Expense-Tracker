from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_index, name='category_index'),
]