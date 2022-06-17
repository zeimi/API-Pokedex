from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('buscar/', views.buscar, name='buscar'),
    path('criar/', views.criar, name='criar'),
    path('inserir/', views.inserir, name='inserir'),
    
]