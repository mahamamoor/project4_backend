from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import FinancialSerializer
from .models import Financial

class FinancialList(generics.ListCreateAPIView):
    queryset = Financial.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = FinancialSerializer # tell django what serializer to use

class FinancialDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Financial.objects.all().order_by('id')
    serializer_class = FinancialSerializer
