from django.urls import path
from . import views
from .views import (
    TransactionExpenseListView,
    TransactionExpenseCreateView,
    TransactionExpenseEditView,
    TransactionExpenseDeleteView,
)


urlpatterns = [
    path("", TransactionExpenseListView.as_view(), name="transactions"),
    path("add/", TransactionExpenseCreateView.as_view(), name="add_transaction"),
    path(
        "<int:pk>/edit", TransactionExpenseEditView.as_view(), name="edit_transaction"
    ),
    path("<int:pk>/delete", TransactionExpenseDeleteView.as_view()),
    path("pie_chart/", views.transaction_expense_pie_chart, name="pie-chart"),
]
