from django.urls import path
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from .views import *

urlpatterns =[
    path('', index, name = 'home'),
    path('solutions/', solutions, name='solutions'),
    path('services/', services, name = "services"),
]