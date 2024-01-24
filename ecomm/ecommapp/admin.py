from django.contrib import admin
from ecommapp.models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=['id','name','price','category','pdeatils','is_Active']
    # displa as table uppar hai
    list_filter=(['category','is_Active'])
admin.site.register(Product,ProductAdmin)
