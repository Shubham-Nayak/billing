from django.db import models
from colorfield.fields import ColorField
from datetime import datetime

# Create your models here.

class Mysetting(models.Model):
    title= models.CharField(default="MyApp",max_length=200,blank=True)
    about_description= models.TextField(blank=True)
    seo_keywords= models.TextField(blank=True)
    phone= models.CharField(max_length=20,blank=True)
    email= models.CharField(max_length=50,blank=True)
    facbook= models.CharField(max_length=50,blank=True)
    instagram= models.CharField(max_length=50,blank=True)
    twitter= models.CharField(max_length=50,blank=True)
    theme_color= ColorField(default='#10284e',blank=True)
    logo=models.ImageField(upload_to='photos/img/',blank=True)
    address=models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title= models.CharField(max_length=200,error_messages={'required': 'Please enter category name'})
    list_date=models.DateTimeField(default=datetime.now,blank=True)
    def __str__(self):
        return self.title
          

class ProductListing(models.Model):
    HSN_Code=models.CharField(max_length=200,unique=True,error_messages={'required': 'Please enter HSN Code'})
    category= models.ForeignKey(Category,on_delete=models.DO_NOTHING)
    title= models.CharField(max_length=200)
    description= models.CharField(blank=True,max_length=500)
    seeling_price= models.IntegerField()
    buying_price= models.IntegerField(default=0)
    available_quantity= models.IntegerField(blank=True)
    gram= models.DecimalField(max_digits=2,decimal_places=1)
    discount= models.IntegerField(default=0)
    photo_main=models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_2=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_3=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_4=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_5=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_6=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    is_published=models.BooleanField(default=True)
    list_date=models.DateTimeField(default=datetime.now,blank=True)
    def __str__(self):
        return self.HSN_Code

