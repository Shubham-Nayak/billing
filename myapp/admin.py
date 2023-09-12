from django.contrib import admin
from .models import Mysetting,ProductListing,Category

class ProductListingAdmin(admin.ModelAdmin):
    list_display=('id','title','seeling_price','is_published','list_date','category','HSN_Code','available_quantity')
    list_display_links=('id','title')
    list_filter=('category',)
    list_editable=('is_published','seeling_price','HSN_Code','available_quantity')
    search_fields=('title',)
    list_per_page=20



admin.site.register(ProductListing,ProductListingAdmin)
admin.site.register(Mysetting)
admin.site.register(Category)



