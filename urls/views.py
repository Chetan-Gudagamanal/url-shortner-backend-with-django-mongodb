from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.views import APIView
from mongo_auth.permissions import AuthenticatedOnly
from rest_framework.response import Response
from rest_framework import status
from mongo_auth.db import database
from shortuuid import uuid

from .serializers import UrlSerializer


# Create your views here.
class GetUrls(APIView):
    permission_classes = [AuthenticatedOnly]

    def get(self, request, format=None):
        try:
            allUrls = list(database["urls"].find({}, {"_id": 0}).limit(10))
            print(allUrls)
            print("===============")
            print(uuid())
            return Response(allUrls, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


class AddUrl(APIView):
    permission_classes = [AuthenticatedOnly]

    def post(self, request: Request):
        try:
            shortId = uuid()
            print(request.data['long_url'])
            record = {'long_url': request.data['long_url'], 'short_url_code': shortId}
            database["urls"].insert_one(record)
            return Response(UrlSerializer(record).data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_408_REQUEST_TIMEOUT)


class GetOriginalUrl(APIView):
    permission_classes = [AuthenticatedOnly]

    def get(self, request: Request):
        try:
            record=list(database["urls"].find({'short_url_code':request.data['short_url_code']}, {"_id": 0}))[0]
            return Response(UrlSerializer(record).data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
