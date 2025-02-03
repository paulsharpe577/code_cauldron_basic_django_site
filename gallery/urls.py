# filepath: /path/to/your/django/project/gallery/urls.py
from django.urls import path
from .views import gallery

urlpatterns = [
    path('', gallery, name='gallery'),
]