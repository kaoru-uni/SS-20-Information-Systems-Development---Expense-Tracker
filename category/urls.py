from django.urls import path
from .views import CategoryListView, CategoryCreateView, CategoryEditView, CategoryDeleteView

#https://stackoverflow.com/questions/58825832/django-delete-button-is-not-redirecting-to-the-correct-path
urlpatterns = [
    path("", CategoryListView.as_view(), name="categories"),
    path("add/", CategoryCreateView.as_view(), name="add_category"),
    path("<int:pk>/edit", CategoryEditView.as_view(), name="edit_category"),
    path("<int:pk>/deletecategory", CategoryDeleteView.as_view()),
]