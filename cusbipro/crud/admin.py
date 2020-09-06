"""
=======================================
Registering models:
Client, Bill, Product and BillProduct
=======================================
"""

# Django
from django.contrib import admin

# Models
from crud.models import Client, Bill, BillProduct, Product

admin.site.register(Client)
admin.site.register(Bill)
admin.site.register(BillProduct)
admin.site.register(Product)