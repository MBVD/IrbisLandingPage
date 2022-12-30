from django.shortcuts import render
from django.http import HttpResponse 
from .models import *

# Create your views here.
def index(request):
    cards = Card.objects.all()
    return render(request, 'index.html', {'title':'Домашняя страница',
                                          'cards': cards,})

def about(request):
    return render(request, 'about.html', {'title': 'О нас'})

def solutions(request):
    return render(request, 'solutions.html', {'title': 'Решения'})

def services(request):
    service = Service.objects.all().first()
    return render(request, 'services.html', {'title': 'Услуги',
                                             'service': service})