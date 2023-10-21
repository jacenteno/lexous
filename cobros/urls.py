from django.urls import path, include
from cobros import views
path('index/', views.index, name='index'),
