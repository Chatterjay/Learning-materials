from django.urls import path
from . import views

urlpatterns = [
    path('aaa/', views.stacked_area_chart_view,name='index'),
]
