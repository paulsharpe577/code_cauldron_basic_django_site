# main/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')

from .models import House

def house_list(request):
    houses = House.objects.all()
    total_price = sum(house.price for house in houses)
    return render(request, 'pages/house_list.html', {'houses': houses, 'total_price': total_price})


