# Generated by Django 3.2.12 on 2023-09-14 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_productlisting_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='mysetting',
            name='address',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
