from django.shortcuts import render
import json

# Create your views here.
from rest_framework import generics
from .serializers import ShopSerializer
from .models import Shop
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from .serializers import UserAccountSerializer
from .models import Account


class UserAccountList(generics.ListCreateAPIView):
    queryset = Account.objects.all().order_by('id')
    serializer_class = AccountSerializer


class UserAccountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all().order_by('id')
    serializer_class = AccountSerializer

def check_login(request):
    if request.method=='GET':
        return JsonResponse({})
        if request.method=='PUT':

        jsonRequest = json.loads(request.body)
        email = jsonRequest['name']
        password = jsonRequest['password']
        if Account.objects.get(email=email):
            user = Account.objects.get(name=name)  
            if check_password(password, user.password):
                return JsonResponse({'id': user.id, 'email': user.name}) 
            else:
                return JsonResponse({})
        else:
            return JsonResponse({})