from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('api/shop', views.ShopList.as_view(), name='shop'),
    path('api/shop/<int:pk>', views.ShopDetail.as_view(), name='shop_detail'), 
]

urlpatterns += staticfiles_urlpatterns()