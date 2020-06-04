from django.db import models
from django.urls import reverse


class Category(models.Model):
    """
    | The following sources has been used:
    | https://stackoverflow.com/questions/323763/foreign-key-from-one-app-into-another-in-django
    | https://stackoverflow.com/questions/26185687/you-are-trying-to-add-a-non-nullable-field-new-field-to-userprofile-without-a
    | This model contains the category of a budget which is defined.
    | name: The category name is set by the user.
    | created_date: is set automatically by django.
    | FK user: The user will be automatically set by django.
    """
    name = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    def __str__(self):
        """
        | Returns self.name instead of object.object
        """
        return str(self.name)

    def get_absolute_url(self):
        return reverse("category-detail", kwargs={"pk": self.pk})
