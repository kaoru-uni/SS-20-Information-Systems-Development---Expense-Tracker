from django.db import models


class Budget(models.Model):
    name = models.CharField(max_length=50)
    amount = models.FloatField()
    description = models.CharField(max_length=200)

    # category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def add(self):
        self.save()


