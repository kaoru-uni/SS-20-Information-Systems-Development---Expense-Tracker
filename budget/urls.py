from django.urls import path

from . import views
from .views import BudgetCreateView, BudgetEditView, BudgetDeleteView
from django.contrib.auth.decorators import login_required

# https://stackoverflow.com/questions/28555260/django-login-required-for-class-views


# https://stackoverflow.com/questions/58825832/django-delete-button-is-not-redirecting-to-the-correct-path
urlpatterns = [
    path("budget_add/", login_required(BudgetCreateView.as_view()), name="add_budget"),
    path(
        "<int:pk>/budgetedit",
        login_required(BudgetEditView.as_view()),
        name="edit_budget",
    ),
    path("<int:pk>/budgetdelete", login_required(BudgetDeleteView.as_view())),
    path("", login_required(views.budget_pie_chart_data), name="budget-pie-chart"),
]
