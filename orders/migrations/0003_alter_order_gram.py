# Generated by Django 3.2.12 on 2023-09-12 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20230912_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='gram',
            field=models.DecimalField(decimal_places=1, max_digits=4),
        ),
    ]