from django.contrib import admin
from .models import *


class CardAdmin(admin.ModelAdmin):
    list_display = ('pretitle', 'title', 'content')
    list_display_links = ('pretitle', 'title', 'content')

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)

admin.site.register(Card, CardAdmin)
admin.site.register(Service, ServiceAdmin)