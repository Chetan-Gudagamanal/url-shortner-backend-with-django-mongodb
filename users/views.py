from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from mongo_auth.permissions import AuthenticatedOnly
from rest_framework.response import Response
from rest_framework import status

class GetTest(APIView):

    permission_classes = [AuthenticatedOnly]

    def get(self, request, format=None):
        try:
            print(request.user)  # This is where magic happens
            return Response(status=status.HTTP_200_OK,
                            data={"data": {"msg": "User Authenticated"}})
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
