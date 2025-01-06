# main/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')


from .models import House

def house_list(request):
    houses = House.objects.all()
    return render(request, 'house_list.html', {'houses': houses})


