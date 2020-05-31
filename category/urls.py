from django.urls import path
from .views import CategoryListView, CategoryCreateView

urlpatterns = [
    path("", CategoryListView.as_view(), name="categories"),
    path("add/", CategoryCreateView.as_view(), name="add_category"),
]