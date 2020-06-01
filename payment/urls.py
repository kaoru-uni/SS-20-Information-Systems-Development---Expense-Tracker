from django.urls import path
from .views import (
    PaymentCreateView,
    PaymentListView,
    PaymentEditView,
    PaymentDeleteView,
)


urlpatterns = [
    path("", PaymentListView.as_view(), name="payment"),
    path("add/", PaymentCreateView.as_view(), name="add_payment"),
    path("<int:pk>/edit", PaymentEditView.as_view(), name="edit_payment"),
    path("<int:pk>/delete", PaymentDeleteView.as_view()),
]
