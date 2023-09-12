from django.db import models
from datetime import datetime
from myapp.models import ProductListing

# Create your models here.

class Order(models.Model):
    HSN_Code= models.ForeignKey(ProductListing,on_delete=models.DO_NOTHING)
    name= models.CharField(max_length=200)
    phone= models.CharField(max_length=20)
    email= models.CharField(max_length=50)
    seeling_price= models.IntegerField(default=0)
    discounted_price= models.IntegerField(default=0)
    gram= models.DecimalField(max_digits=4,decimal_places=1)
    purchase_date=models.DateTimeField(default=datetime.now,blank=True)
    user_id= models.IntegerField(blank=True,default=0)
    purchase_mode= models.CharField(default='offline',max_length=100)
    saller= models.CharField(default='shop',max_length=200)


    def __str__(self):
        return self.name







    



