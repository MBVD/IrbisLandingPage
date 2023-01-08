from django.shortcuts import render
from django.http import HttpResponse 
from .models import *

# Create your views here.
def index(request):
    cards = Card.objects.filter(for_solution = False)
    return render(request, 'index.html', {'title':'Домашняя страница',
                                          'cards': cards,})

def about(request):
    return render(request, 'about.html', {'title': 'О нас'})

def solutions(request):
    cards = Card.objects.filter(for_solution = True)
    return render(request, 'solutions.html', {'title': 'Решения',
                                              'cards': cards,
                                             })

def services(request):
    service = Service.objects.all().first()
    return render(request, 'services.html', {'title': 'Услуги',
                                             'service': service})