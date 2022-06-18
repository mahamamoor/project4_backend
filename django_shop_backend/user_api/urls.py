from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt



urlpatterns = [
    path('api/useraccount', views.AccountList.as_view(), name='useraccount_list'),
    path('api/useraccount/<int:pk>', views.AccountDetail.as_view(), name='useraccount_detail'),
    path('api/useraccount/login', csrf_exempt(views.check_login), name="check_login")
]

