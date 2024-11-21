from django.urls import path
from .views import get_sales_data

urlpatterns = [
    path('', get_sales_data, name='car_sales'),
]