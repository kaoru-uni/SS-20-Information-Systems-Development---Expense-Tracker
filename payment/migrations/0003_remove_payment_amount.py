# Generated by Django 3.0.5 on 2020-06-02 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_auto_20200601_1226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='amount',
        ),
    ]
