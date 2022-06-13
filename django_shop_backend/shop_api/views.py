from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import ShopSerializer
from .models import Shop

class ShopList(generics.ListCreateAPIView):
    queryset = Shop.objects.all().order_by('id')
    serializer_class = ShopSerializer
    
class ShopDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shop.objects.all().order_by('id')
    serializer_class = ShopSerializer
