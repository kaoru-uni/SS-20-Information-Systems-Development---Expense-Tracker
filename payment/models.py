from django.db import models

# Create your models here.
from django.db import models


class PaymentConfig(models.Model):
    type = models.CharField(max_length=50)
    date = models.DateTimeField()
    amount = models.CharField(max_length=200)

    def add(self):
        self.save()
