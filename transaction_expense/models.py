from django.db import models

"""
This model contains the transaction of an expense which is being made.
A transaction can be made by a family member.
"""


class Transaction_Expense(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    family = models.BooleanField()
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
