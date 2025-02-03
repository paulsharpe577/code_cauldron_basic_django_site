# filepath: /path/to/your/django/project/gallery/admin.py
from django.contrib import admin
from .models import Image

admin.site.register(Image)