"""
=======================================
Serializers class/models:
Client, Bill, Product and BillProduct
=======================================
"""

# Django
from rest_framework import serializers

# Local app crud
from crud.models import Client, Bill, Product, BillProduct


class ClientSerializer(serializers.Serializer):
    """ Serializer class for client class"""
    id = serializers.IntegerField(read_only=True)
    document = serializers.IntegerField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()

    def create(self, validated_data):
        """ Create and return a new Client instance"""
        return Client.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """Update and return an existing Client instance"""
        instance.document = validated_data.get('document',
                                               instance.document)
        instance.first_name = validated_data.get('first_name',
                                                 instance.first_name)
        instance.last_name = validated_data.get('last_name',
                                                instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

class BillSerializer(serializers.ModelSerializer):
    """ Serializer class for Bill class"""

    class Meta:
        model = Bill
        fields = ['id', 'client_id', 'company_name', 'nit', 'code']

class ProductSerializer(serializers.Serializer):
    """ Serializer class for Product class"""
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()

    def create(self, validated_data):
        """ Create and return a new Product instance"""
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """Update and return an existing Product instance"""
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description',
                                                  instance.description)
        instance.save()
        return instance

class BillProductSerializer(serializers.ModelSerializer):
    """ Serializer class for BillProduct class"""
    bill_id = BillSerializer(read_only=True)
    product_id = ProductSerializer(read_only=True)

    class Meta:
        model = BillProduct
        fields = ['bill_id', 'product_id']
