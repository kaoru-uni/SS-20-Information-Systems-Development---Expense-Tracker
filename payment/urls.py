from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import (
    PaymentCreateView,
    PaymentListView,
    PaymentEditView,
    PaymentDeleteView,
)

"""
| The following source has been used:
| https://stackoverflow.com/questions/28555260/django-login-required-for-class-views
| login_required: Enforces that the user is logged in.
"""
urlpatterns = [
    path("", login_required(PaymentListView.as_view()), name="payment"),
    path("add/", login_required(PaymentCreateView.as_view()), name="add_payment"),
    path("<int:pk>/edit", login_required(PaymentEditView.as_view()), name="edit_payment"),
    path("<int:pk>/delete", login_required(PaymentDeleteView.as_view())),
]
