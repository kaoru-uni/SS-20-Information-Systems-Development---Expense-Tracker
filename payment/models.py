from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


# https://docs.djangoproject.com/en/3.0/ref/models/fields/#choices
class Payment(models.Model):
    VISA = "VISA"
    MASTERCARD = "MASTERCARD"
    BANK = "BANK"
    CRYPTO = "CRYPTO"
    CASH = "CASH"
    PAYMENT_TYPE = [
        (CASH, "Cash"),
        (VISA, "Visa"),
        (MASTERCARD, "Mastercard"),
        (BANK, "Bank"),
        (CRYPTO, "Crypto"),
    ]
    type = models.CharField(max_length=50, choices=PAYMENT_TYPE, default=CASH, )
    date = models.DateTimeField()
    description = models.CharField(max_length=100, default="")
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    def __str__(self):
        return f"Type: {self.type}, Description: {self.description}"
