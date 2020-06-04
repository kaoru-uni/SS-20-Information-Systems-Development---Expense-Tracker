from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views
from .views import (
    TransactionExpenseListView,
    TransactionExpenseCreateView,
    TransactionExpenseEditView,
    TransactionExpenseDeleteView,
)

"""
| The following source has been used:
| https://stackoverflow.com/questions/28555260/django-login-required-for-class-views
| login_required: Enforces that the user is logged in.
"""
urlpatterns = [
    path("", login_required(TransactionExpenseListView.as_view()), name="transactions"),
    path(
        "add/",
        login_required(TransactionExpenseCreateView.as_view()),
        name="add_transaction",
    ),
    path(
        "<int:pk>/edit",
        login_required(TransactionExpenseEditView.as_view()),
        name="edit_transaction",
    ),
    path("<int:pk>/delete", login_required(TransactionExpenseDeleteView.as_view())),
    path(
        "pie_chart/",
        login_required(views.transaction_expense_pie_chart),
        name="pie-chart",
    ),
]
