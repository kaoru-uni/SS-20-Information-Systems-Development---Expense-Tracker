# Generated by Django 3.0.5 on 2020-06-01 17:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('transaction_expense', '0003_transaction_expense_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction_expense',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='transaction_expense',
            name='updated_date',
        ),
        migrations.AddField(
            model_name='transaction_expense',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
