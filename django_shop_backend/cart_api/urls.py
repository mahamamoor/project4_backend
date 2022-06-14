from django.urls import path
from . import views

urlpatterns = [
    path('api/cart', views.CartList.as_view(), name='cart_list'),
    path('api/cart/<int:pk>', views.CartDetail.as_view(), name='cart_detail'),
]
