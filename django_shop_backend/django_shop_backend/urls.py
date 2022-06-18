from django.contrib import admin
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from django.conf.urls import include

urlpatterns = [
    path('', include('shop_api.urls')),
    path('', include('cart_api.urls')),
    path('admin/', admin.site.urls),
]


urlpatterns = [
   
    path('core/', include('core.urls'))
]