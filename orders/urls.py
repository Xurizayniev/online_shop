from django.urls import path
from .views import *


app_name = 'orders'

urlpatterns = [
    path('history/', OrderHistoryView.as_view(), name='history'),
    path('checkout/', CheckoutView.as_view(), name='checkout')
]
