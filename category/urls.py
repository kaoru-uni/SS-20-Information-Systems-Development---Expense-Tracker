from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import CategoryListView, CategoryCreateView, CategoryEditView, CategoryDeleteView

"""
| The following source has been used:
| https://stackoverflow.com/questions/28555260/django-login-required-for-class-views
| https://stackoverflow.com/questions/58825832/django-delete-button-is-not-redirecting-to-the-correct-path
| login_required: Enforces that the user is logged in.
"""
urlpatterns = [
    path("", login_required(CategoryListView.as_view()), name="categories"),
    path("add/", login_required(CategoryCreateView.as_view()), name="add_category"),
    path("<int:pk>/edit", login_required(CategoryEditView.as_view()), name="edit_category"),
    path("<int:pk>/delete", login_required(CategoryDeleteView.as_view())),
]
