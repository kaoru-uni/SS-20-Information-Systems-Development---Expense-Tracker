from django.urls import path
from .views import TransactionExpenseListView, TransactionExpenseCreateView


urlpatterns = [
    path("", TransactionExpenseListView.as_view(), name="transactions"),
    path("add/", TransactionExpenseCreateView.as_view(), name="add_transaction"),
]
