from django.contrib import admin
from .models import *

# Register your models here.

# class CustomerAdmin(admin.ModelAdmin):
#     list_display = ('user','name')
admin.site.register(Customer)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name','price','digital')
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(OrderPlaced)
admin.site.register(Category)


