from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save


class UserProfileSettingConfig(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=200, default='')
    phone = models.IntegerField(default=0)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfileSettingConfig.objects.create(user=instance)


post_save.connect(create_user_profile, sender=User)
