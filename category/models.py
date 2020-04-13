from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def add(self):
        self.save()