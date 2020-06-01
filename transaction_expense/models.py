from django.db import models
from category.models import Category

"""
This model contains the transaction of an expense which is being made.
A transaction can be made by a family member.
"""

# https://stackoverflow.com/questions/323763/foreign-key-from-one-app-into-another-in-django
# https://stackoverflow.com/questions/26185687/you-are-trying-to-add-a-non-nullable-field-new-field-to-userprofile-without-a
class Transaction_Expense(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    family = models.BooleanField()
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)