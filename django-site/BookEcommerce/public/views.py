# frontend/views.py

from django.shortcuts import render
import requests

def index(request):
    response = requests.get('http://api:8001/api/books/')
    books = response.json()
    return render(request, 'index.html', {'books': books})

def detail(request, id):
    return render(request, 'detail.html', {'id': id})
