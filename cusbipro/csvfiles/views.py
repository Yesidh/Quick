"""
=======================================
Class-based views for:
exports Client models in a csv file
=======================================
"""
# Python
import csv

# Django
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from django.http import HttpResponse

# Local app users
from crud.models import Client, Bill

class CsvView(APIView):
    """ generate Clients models in a csv file"""

    def get(self, request):
        """ generate Clients models in a csv file"""

        permission_classes = (IsAuthenticated, )

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; ' \
                                          'filename="clientList.csv"'
        writer = csv.DictWriter(response, fieldnames=['Document',
                                                      'Full Name',
                                                      'Count of Bill'])
        writer.writeheader()
        clientList = Client.objects.raw('SELECT * FROM crud_client')
        for client in clientList:
            billsCount = Bill.objects.filter(client_id=client.id).count()
            writer.writerow({'Document': client.document,
                             "Full Name": client.first_name + ' '
                                          + client.last_name,
                             'Count of Bill': billsCount})
        return response

class CsvUploadFile(APIView):
    """ Upload a csv file and create Client instances with data """

    parser_classes = (FileUploadParser, )

    def put(self, request, filename, format='.csv'):
        """ Create Client instances from a file"""

        file_obj = request.data['file']
        import pdb; pdb.set_trace()