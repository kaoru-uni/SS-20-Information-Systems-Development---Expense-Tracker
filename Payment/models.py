from django.db import models


class Payment(models.Model):
    type = models.CharField(max_length=50)
    date = models.DateField()
    amount = models.CharField(max_length=200)

    def add(self):
        self.save()
