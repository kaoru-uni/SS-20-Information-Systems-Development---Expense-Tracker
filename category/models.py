from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('category-detail', kwargs={'pk': self.pk})