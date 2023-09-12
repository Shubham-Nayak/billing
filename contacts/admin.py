from django.contrib import admin
from .models import Contact
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display=('id','name','product_name','email','phone','contact_date')
    list_display_links=('id','name')
    search_fields=('name','phone','email','product_name')
    list_per_page=20
admin.site.register(Contact,ContactAdmin)