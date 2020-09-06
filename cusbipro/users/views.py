"""
=======================================
Class-based views for:
User
=======================================
"""

# Django
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Local app users
from users.serializers import UserSerializer


class CreateUser(APIView):
    """ Create a user instance and return it"""

    def post(self, request):
        """ Create a user instance an return it"""
        user = request.data
        user['username'] = request.data['email']
        serializer = UserSerializer(data=user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
