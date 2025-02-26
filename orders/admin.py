from django.contrib import admin
from .models import Product, Customer, Seller, Order, PlatformApiCall

# Register the models with the Django admin site
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Seller)
admin.site.register(Order)
admin.site.register(PlatformApiCall)
