# frontend/urls.py

from django.urls import path
from .views import index, detail


urlpatterns = [
    path('', index, name='index'),
    path('<int:id>', detail, name='detail'),
]
