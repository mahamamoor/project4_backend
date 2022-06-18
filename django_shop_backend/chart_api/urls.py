from django.urls import path
from . import views

urlpatterns = [
    path('api/financials', views.FinancialList.as_view(), name='financial_list'),
    path('api/financial/<int:pk>', views.FinancialDetail.as_view(), name='financial_detail'),
]
