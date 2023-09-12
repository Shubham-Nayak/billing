from django.contrib import admin
from .models import Order
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display=('id','name','HSN_Code','email','phone','discounted_price','discounted_price')
    list_display_links=('id','name')
    list_filter=('purchase_date','HSN_Code')
    list_editable=('email','discounted_price','HSN_Code','phone')
    search_fields=('name','phone')
    list_per_page=20
admin.site.register(Order,OrderAdmin)