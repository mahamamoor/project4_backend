from django.urls import path
from . import views

urlpatterns = [
    path('api/shop', views.ShopList.as_view(), name='shop'),
    path('api/shop/<int:pk>', views.ShopDetail.as_view(), name='shop_detail'), 
]
