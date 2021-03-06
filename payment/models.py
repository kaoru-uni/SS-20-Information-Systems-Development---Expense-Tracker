from django.contrib.auth.models import User
from django.db import models


# https://docs.djangoproject.com/en/3.0/ref/models/fields/#choices
class Payment(models.Model):
    """
    | This class represents the model for the payment options.
    | PAYMENT_TYPE: A user chan choose from the available options.
    """
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
        """
        | Returns the interpolated string instead of object.object
        """
        return f"Type: {self.type}, Description: {self.description}"
