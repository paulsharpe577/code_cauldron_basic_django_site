# main/urls.py
from django.urls import path
from . import views
from .views import house_list

urlpatterns = [
    path('', views.home, name='home'),
    path('house_list', house_list, name='house_list'),
]