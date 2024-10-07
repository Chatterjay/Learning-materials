from django.urls import path,include

from . import views

urlpatterns =[
    path("hw",views.hw,name='index'),
]
