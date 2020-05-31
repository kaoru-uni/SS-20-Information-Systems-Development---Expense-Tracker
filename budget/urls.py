from django.urls import path
from .views import BudgetListView, BudgetCreateView, BudgetEditView, BudgetDeleteView

#https://stackoverflow.com/questions/58825832/django-delete-button-is-not-redirecting-to-the-correct-path
urlpatterns = [
    path("", BudgetListView.as_view(), name="budgets"),
    path("budget_add/", BudgetCreateView.as_view(), name="add_budget"),
    path("<int:pk>/budgetedit", BudgetEditView.as_view(), name="edit_budget"),
    path("<int:pk>/budgetdelete", BudgetDeleteView.as_view()),
]