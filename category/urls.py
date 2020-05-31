from django.urls import path
from . import views
from category.views import HomeViewClass

urlpatterns = [
    path('', views.categories, name='categories'),
]