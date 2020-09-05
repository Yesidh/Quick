"""
============================
Class-based views for:
Client, Bill, Product and BillProduct
=======================================
"""

# Django
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
# Local app crud
from crud.models import Client, Bill, Product, BillProduct
from crud.serializers import ClientSerializer, BillSerializer,\
    ProductSerializer, BillProductSerializer

class ClientView(APIView):
    """ Create, Retrieve, Update and Delete a Client instance """

    #permission_classes = (IsAuthenticated, )

    def post(self, request, format=None):
        """ Create and Return a Client instance """
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        """Retrieve all Client instances"""
        listClients = Client.objects.raw('SELECT * FROM crud_client')
        serializer = ClientSerializer(listClients, many=True)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """ Update and Return a Client instance"""
        clientUpdate = Client.objects.raw(f'SELECT * FROM crud_client WHERE id = {pk}')
        serializer = ClientSerializer(clientUpdate[0], data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """ Delete a Client instance"""
        clientDelete = Client.objects.raw(f'SELECT * FROM crud_client WHERE id = {pk}')
        if clientDelete:
            clientDelete[0].delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"errors": "Client doesn't exist"}, status=status.HTTP_400_BAD_REQUEST)


class BillView(APIView):
    """ Create, Retrieve, Update and Delete a Bill instance """

    #permission_classes = (IsAuthenticated, )

    def post(self, request, format=None):
        """ Create and Return a Bill instance """
        serializer = BillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        """Retrieve all Bill instances"""
        listBills = Bill.objects.raw('SELECT * FROM crud_bill')
        serializer = BillSerializer(listBills, many=True)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """ Update and Return a Bill instance"""
        billUpdate = Bill.objects.raw(f'SELECT * FROM crud_bill WHERE id = {pk}')
        serializer = BillSerializer(billUpdate[0], data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """ Delete a Bill instance"""
        billDelete = Bill.objects.raw(f'SELECT * FROM crud_bill WHERE id = {pk}')
        if billDelete:
            billDelete[0].delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"errors": "Bill doesn't exist"}, status=status.HTTP_400_BAD_REQUEST)

class ProductView(APIView):
    """ Create, Retrieve, Update and Delete a Product instance """

    #permission_classes = (IsAuthenticated, )

    def post(self, request, format=None):
        """ Create and Return a Product instance """
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        """Retrieve all Product instances"""
        listProducts = Product.objects.raw('SELECT * FROM crud_product')
        serializer = ProductSerializer(listProducts, many=True)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """ Update and Return a Product instance"""
        productUpdate = Product.objects.raw(f'SELECT * FROM crud_product WHERE id = {pk}')
        serializer = ProductSerializer(productUpdate[0], data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """ Delete a Product instance"""
        productDelete = Product.objects.raw(f'SELECT * FROM crud_product WHERE id = {pk}')
        if productDelete:
            productDelete[0].delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"errors": "Product doesn't exist"}, status=status.HTTP_400_BAD_REQUEST)


class BillProductView(APIView):
    """ Create, Retrieve, Update and Delete a Product instance """

    #permission_classes = (IsAuthenticated, )

    def post(self, request, format=None):
        """ Create and Return a BillProduct instance """
        serializer = BillProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        """Retrieve all Bill Product instances"""
        listBillProducts = BillProduct.objects.raw('SELECT * FROM crud_billproduct')
        import pdb; pdb.set_trace()
        serializer = BillProductSerializer(listBillProducts, many=True)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """ Update and Return a BillProduct instance"""
        billProductUpdate = BillProduct.objects.raw(f'SELECT * FROM crud_billproduct WHERE id = {pk}')
        serializer = BillProductSerializer(billProductUpdate[0], data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """ Delete a BillProduct instance"""
        billProductDelete = BillProduct.objects.raw(f'SELECT * FROM crud_billproduct WHERE id = {pk}')
        if billProductDelete:
            billProductDelete[0].delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"errors": "Product doesn't exist"}, status=status.HTTP_400_BAD_REQUEST)
