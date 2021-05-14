# formatter/urls.py
from django.urls import path # Add this
from . import views # Add this

# Add this
urlpatterns = [
    path('', views.index, name = 'index')
]