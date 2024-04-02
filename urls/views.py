from django.shortcuts import render
from rest_framework.views import APIView
from mongo_auth.permissions import AuthenticatedOnly
from rest_framework.response import Response
from rest_framework import status
from mongo_auth.db import database


# Create your views here.
class GetUrls(APIView):
    permission_classes = [AuthenticatedOnly]

    def get(self, request, format=None):
        try:
            print(list(database["urls"].find({}, {"_id": 0}).limit(10)))
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
