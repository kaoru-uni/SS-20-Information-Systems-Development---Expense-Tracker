from django.db import models

from category.models import Category


class Budget(models.Model):
    """
    | The following sources has been used:
    | https://stackoverflow.com/questions/323763/foreign-key-from-one-app-into-another-in-django
    | https://stackoverflow.com/questions/26185687/you-are-trying-to-add-a-non-nullable-field-new-field-to-userprofile-without-a
    | This model contains the budget of an expense which is being made.
    | name: The budget name is set by the user.
    | amount: Amount of the value which the budget has per month.
    | description: A description to remember what the budget was about.
    | date: is set automatically by django.
    | FK user: The user will be automatically set by django.
    | FK category: Choose from the user created categories.
    """
    name = models.CharField(max_length=50)
    amount = models.FloatField(null=True)
    description = models.CharField(max_length=200)

    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.name)
