"""
=======================================
Creating model class:
Client, Bill, Product and BillProduct
=======================================
"""

# Django
from django.db import models


class Client(models.Model):
    """
    Client model.
    """
    document = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return clients first name"""

        return "{}, with document: {} ".format(self.first_name, self.document)


class Bill(models.Model):
    """
    Bills model.
    """
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=70)
    nit = models.IntegerField()
    code = models.IntegerField()

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return company name"""

        return "{}, with code: {} ".format(self.company_name, self.code)


class Product(models.Model):
    """
    Product model
    """
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=150)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return product name"""

        return self.name


class BillProduct(models.Model):
    """
    Bill product model
    """
    bill_id = models.ForeignKey(Bill, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return Bill id"""

        return str(self.bill_id)
