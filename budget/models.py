from django.db import models


class Budget(models.Model):
    name = models.CharField(max_length=50)
    amount = models.FloatField()
    description = models.CharField(max_length=200)
<<<<<<< HEAD

    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
=======
    #category = models.ForeignKey('category.Category', on_delete=models.CASCADE)
>>>>>>> 580d0b8822608b66c4fb6e68dbabb8e4a4b86ff4

    def add(self):
        self.save()


