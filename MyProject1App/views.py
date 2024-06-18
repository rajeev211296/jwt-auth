from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets

# Create your views here.

class ModelViewset(viewsets.ModelViewSet):
    queryset = ItemModel.objects.all()
    serializer_class = ModelSerialzer
