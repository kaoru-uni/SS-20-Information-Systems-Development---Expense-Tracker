from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# https://docs.djangoproject.com/en/3.0/ref/models/fields/#choices
class Payment(models.Model):
    VISA = "VISA"
    MASTERCARD = "MASTERCARD"
    CASH = "CASH"
    PAYMENT_TYPE = [
        (CASH, "Cash"),
        (VISA, "Visa"),
        (MASTERCARD, "Mastercard"),
    ]
    type = models.CharField(max_length=50, choices=PAYMENT_TYPE, default=CASH,)
    date = models.DateTimeField()
    description = models.CharField(max_length=100, default="")
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    def __str__(self):
        return (
            f"Type: {self.type}, Description: {self.description}, Amount: {self.amount}"
        )
