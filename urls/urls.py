from django.urls import path

from . import views
from rest_framework.views import APIView


urlpatterns = [
    path('',views.GetUrls.as_view()),
    path('add/',views.AddUrl.as_view()),
    path('redirecturl/',views.GetOriginalUrl.as_view()),
]