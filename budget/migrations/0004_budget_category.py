# Generated by Django 3.0.6 on 2020-06-01 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0004_category_created_date'),
        ('budget', '0003_auto_20200531_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='budget',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='category.Category'),
        ),
    ]
