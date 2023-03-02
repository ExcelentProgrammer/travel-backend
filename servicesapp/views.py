from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from .models import ServicesModel
from .serializers import ServicesSerializer


# Create your views here.


class getAllServices(ListAPIView):
    queryset = ServicesModel.objects.all()
    serializer_class = ServicesSerializer


class oneServicesAPIView(RetrieveAPIView):
    queryset = ServicesModel.objects.all()
    serializer_class = ServicesSerializer
    lookup_field = "id"
