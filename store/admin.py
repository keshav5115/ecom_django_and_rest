from django.contrib import admin
from .models import Product, Customer, Order

admin.site.site_header = "ECOMMERCE ADMIN"


class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "quantity", "category"]
    list_filter = ["category"]


admin.site.register(Product, ProductAdmin)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "phone", "address"]


admin.site.register(Customer, CustomerAdmin)


admin.site.register(Order)
