from django.urls import path
from . import views

urlpatterns = [
    path('line-chart/', views.line_chart_view,name='line_chart'),
    path('line-chart2/', views.line_chart_view2,name='line_chart2'),
    path('line-chart3/', views.heat_map,name='line_chart3'),
]
