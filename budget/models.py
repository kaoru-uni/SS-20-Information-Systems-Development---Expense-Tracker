from django.db import models
from django.urls import reverse
from category.models import Category


class Budget(models.Model):
    name = models.CharField(max_length=50)
    amount = models.FloatField(null=True)
    description = models.CharField(max_length=200)

    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.name)
