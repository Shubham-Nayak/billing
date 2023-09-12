# Generated by Django 3.2.12 on 2023-09-12 09:35

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(error_messages={'required': 'Please enter category name'}, max_length=200)),
                ('list_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listing', models.CharField(max_length=200)),
                ('listing_id', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('message', models.TextField(blank=True)),
                ('contact_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('user_id', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductListing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HSN_Code', models.CharField(error_messages={'required': 'Please enter HSN Code'}, max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('seeling_price', models.IntegerField()),
                ('buying_price', models.IntegerField(default=0)),
                ('available_quantity', models.IntegerField(blank=True)),
                ('gram', models.DecimalField(decimal_places=1, max_digits=2)),
                ('photo_main', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_5', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_6', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('is_published', models.BooleanField(default=True)),
                ('list_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.category')),
            ],
        ),
    ]