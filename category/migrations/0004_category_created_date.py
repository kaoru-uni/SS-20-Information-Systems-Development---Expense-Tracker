# Generated by Django 3.0.6 on 2020-05-31 14:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_category_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
