# my_genai_webapp/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),          # Admin panel
    path('', include('genai_webapp.urls')),   # Include URLs from the genai_webapp app
]
