from django.db import models
from django.urls import reverse


class Budget(models.Model):
    name = models.CharField(max_length=50)
    amount = models.FloatField()
    description = models.CharField(max_length=200)

    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('budget-detail', kwargs={'pk': self.pk})


