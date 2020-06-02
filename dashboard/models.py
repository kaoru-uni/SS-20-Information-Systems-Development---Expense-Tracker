from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=10, decimal_places=2)


class Transaction(models.Model):
    name = models.CharField(max_length=30)
