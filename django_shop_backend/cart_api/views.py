from django.shortcuts import render
from rest_framework import generics
from .serializers import CartSerializer
from .models import Cart

# Create your views here.
class CartList(generics.ListCreateAPIView):
    queryset = Cart.objects.all().order_by('id')
    serializer_class = CartSerializer

class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all().order_by('id')
    serializer_class = CartSerializer
