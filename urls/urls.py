from django.urls import path

from . import views
from rest_framework.views import APIView


urlpatterns = [
    path('',views.GetUrls.as_view())
]