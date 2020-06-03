from django.db import models
from category.models import Category
from payment.models import Payment


# https://stackoverflow.com/questions/323763/foreign-key-from-one-app-into-another-in-django
# https://stackoverflow.com/questions/26185687/you-are-trying-to-add-a-non-nullable-field-new-field-to-userprofile-without-a
class Transaction_Expense(models.Model):
    """
    | This model contains the transaction of an expense which is being made.
    | date: The date can be set by the user.
    | amount: Amount of the value which was paid.
    | description: A description to remember what was paid.
    | user: The user will be automatically set by django.
    | category: Choose from the user created categories.
    | payment: Choose from the user created payment methods.
    """
    date = models.DateTimeField()
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    description = models.CharField(max_length=200, default="")
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True)
