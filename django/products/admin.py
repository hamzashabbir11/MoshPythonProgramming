from django.contrib import admin
from .models import Product, Discount

# Register your models here.

class prodadmin(admin.ModelAdmin):
    list_display = ('name','price','stock')


class disc(admin.ModelAdmin):
    list_display = ('code','discountt')
    
    

admin.site.register(Product,prodadmin)
admin.site.register(Discount,disc)

